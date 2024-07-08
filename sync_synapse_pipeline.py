# Pre-req : pip install azure-mgmt-synapse azure-identity. Also, ensure necessary Azure credentials set up for DefaultAzureCredential.
# Usage: 
# python sync_synapse_pipeline.py --source_workspace_name source_workspace_name --target_workspace_name target_workspace_name --source_subscription_id source_subscription_id --target_subscription_id target_subscription_id --source_resource_group_name source_resource_group_name --target_resource_group_name target_resource_group_name

import argparse
from azure.identity import DefaultAzureCredential
from azure.mgmt.synapse import SynapseManagementClient
from azure.mgmt.synapse.models import PipelineResource

def list_synapse_pipelines(synapse_client, resource_group_name, workspace_name):
    return synapse_client.pipelines.list_by_workspace(
        resource_group_name=resource_group_name,
        workspace_name=workspace_name
    )

def get_synapse_pipeline(synapse_client, resource_group_name, workspace_name, pipeline_name):
    return synapse_client.pipelines.get(
        resource_group_name=resource_group_name,
        workspace_name=workspace_name,
        pipeline_name=pipeline_name
    )

def put_synapse_pipeline(synapse_client, resource_group_name, workspace_name, pipeline_name, pipeline_body):
    pipeline_resource = PipelineResource(properties=pipeline_body['properties'])
    return synapse_client.pipelines.create_or_update(
        resource_group_name=resource_group_name,
        workspace_name=workspace_name,
        pipeline_name=pipeline_name,
        parameters=pipeline_resource
    )

def main(source_workspace_name, target_workspace_name, source_subscription_id, target_subscription_id, source_resource_group_name, target_resource_group_name):
    credential = DefaultAzureCredential()

    # Source Synapse Client
    source_synapse_client = SynapseManagementClient(credential, source_subscription_id)

    # Target Synapse Client
    target_synapse_client = SynapseManagementClient(credential, target_subscription_id)

    try:
        # List all pipelines in the source workspace
        pipelines = list_synapse_pipelines(source_synapse_client, source_resource_group_name, source_workspace_name)
        pipeline_names = [pipeline.name for pipeline in pipelines]
    except Exception as e:
        print(f'Failed to list pipelines from source workspace: {e}')
        return

    for pipeline_name in pipeline_names:
        try:
            # Get the pipeline from the source workspace
            pipeline = get_synapse_pipeline(source_synapse_client, source_resource_group_name, source_workspace_name, pipeline_name)
            pipeline_body = pipeline.as_dict()

            # Write the pipeline to the target workspace
            result = put_synapse_pipeline(target_synapse_client, target_resource_group_name, target_workspace_name, pipeline_name, pipeline_body)
            print(f'Successfully processed {pipeline_name} with result {result}')
        except Exception as e:
            print(f'Failed to process {pipeline_name}: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--source_workspace_name', type=str, required=True, help='The name of the source Synapse workspace.')
    parser.add_argument('--target_workspace_name', type=str, required=True, help='The name of the target Synapse workspace.')
    parser.add_argument('--source_subscription_id', type=str, required=True, help='The Azure subscription ID of the source workspace.')
    parser.add_argument('--target_subscription_id', type=str, required=True, help='The Azure subscription ID of the target workspace.')
    parser.add_argument('--source_resource_group_name', type=str, required=True, help='The Azure resource group name of the source workspace.')
    parser.add_argument('--target_resource_group_name', type=str, required=True, help='The Azure resource group name of the target workspace.')

    args = parser.parse_args()

    main(args.source_workspace_name, args.target_workspace_name, args.source_subscription_id, args.target_subscription_id, args.source_resource_group_name, args.target_resource_group_name)


    args = parser.parse_args()

    main(args.source_workspace_name, args.target_workspace_name, args.subscription_id, args.source_resource_group_name, args.target_resource_group_name)
