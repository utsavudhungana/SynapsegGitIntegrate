#!/bin/bash

# List pipelines and store in an array, removing spaces
mapfile -t pipeline_array < <(az synapse pipeline list --workspace-name $source_workspace_name --query "[].name" -o tsv | sed 's/ //g')

# Loop over the array to get each pipeline and save as .json file
for pipeline in "${pipeline_array[@]}"; 
do
    curl -X GET -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" https://$source_workspace_name.dev.azuresynapse.net/pipelines/$pipeline?api-version=2020-12-01 > "${pipeline}.json";
done

# Loop over the array and put each pipeline to target workspace.
for pipeline in "${pipeline_array[@]}"; 
do
	curl -X PUT -d @$pipeline.json -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" https://$workspace_name.dev.azuresynapse.net/pipelines/$pipeline?api-version=2020-12-01;	
done

# Clean up
for pipeline in "${pipeline_array[@]}"; 
do
	rm $pipeline.json;
done