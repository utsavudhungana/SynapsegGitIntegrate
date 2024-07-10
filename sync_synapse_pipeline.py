# Pre-req : pip install azure-mgmt-synapse azure-identity. Also, ensure necessary Azure credentials set up for DefaultAzureCredential.
# Usage: python sync_synapse_pipeline.py --source_workspace_name source_workspace_name --target_workspace_name target_workspace_name
# Authored By: Utsav Dhungana

import argparse
from azure.identity import DefaultAzureCredential
from azure.synapse.artifacts import ArtifactsClient
from azure.core.exceptions import HttpResponseError

def list_synapse_pipelines(client):
    try:
        pipelines = client.pipeline.get_pipelines_by_workspace()
        return [pipeline.name for pipeline in pipelines]
    except HttpResponseError as err:
        print(f"Failed to list pipelines: {err}")
        return []

def get_synapse_pipeline(client, pipeline_name):
    try:
        pipeline = client.pipeline.get_pipeline(pipeline_name)
        return pipeline
    except HttpResponseError as err:
        print(f"Failed to get pipeline '{pipeline_name}': {err}")
        return None

def put_synapse_pipeline(client, workspace_name, pipeline_name, pipeline):
    try:
        result = client.pipeline.begin_create_or_update_pipeline( pipeline_name, pipeline).result()
        return result
    except HttpResponseError as err:
        print(f"Failed to create/update pipeline '{pipeline_name}': {err}")
        return None

def main(source_workspace_name, target_workspace_name):
    credential = DefaultAzureCredential()

    # Source Artifacts Client
    source_client = ArtifactsClient(credential, f'https://{source_workspace_name}.dev.azuresynapse.net')

    # Target Artifacts Client
    target_client = ArtifactsClient(credential, f'https://{target_workspace_name}.dev.azuresynapse.net')

    try:
        # List all pipelines in the source workspace
        pipeline_names = list_synapse_pipelines(source_client)

        print('List of pipelines in source workspace:') 
        for pipeline_name in pipeline_names:
            print(pipeline_name)

    except Exception as e:
        print(f'Failed to list pipelines from source workspace: {e}')
        return

    for pipeline_name in pipeline_names:
        try:
            # Get the pipeline from the source workspace
            pipeline = get_synapse_pipeline(source_client, pipeline_name)


            # Write the pipeline to the target workspace
            result = put_synapse_pipeline(target_client, target_workspace_name, pipeline_name, pipeline)
            if result:
                print(f'{result}')
        except Exception as e:
            print(f'Failed to process {pipeline_name}: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transfer Synapse pipelines between workspaces.')
    parser.add_argument('--source_workspace_name', type=str, required=True, help='Source Synapse workspace name.')
    parser.add_argument('--target_workspace_name', type=str, required=True, help='Target Synapse workspace name.')

    args = parser.parse_args()

    main(args.source_workspace_name, args.target_workspace_name)
