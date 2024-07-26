#!/bin/bash

# List datasets and store in an array, removing spaces
mapfile -t dataset_array < <(az synapse dataset list --workspace-name $source_workspace_name --query "[].name" -o tsv | sed 's/ //g')

# Loop over the array to get each dataset and save as .json file
for dataset in "${dataset_array[@]}"; 
do
    curl -X GET -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" https://$source_workspace_name.dev.azuresynapse.net/datasets/$dataset?api-version=2020-12-01 > "${dataset}.json";
done

# Loop over the array and put each dataset to target workspace.
for dataset in "${dataset_array[@]}"; 
do
	curl -X PUT -d @$dataset.json -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" https://$workspace_name.dev.azuresynapse.net/datasets/$dataset?api-version=2020-12-01;	
done

# Clean up
for dataset in "${dataset_array[@]}"; 
do
	rm $dataset.json;
done