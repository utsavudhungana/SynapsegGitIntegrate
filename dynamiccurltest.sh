#!/bin/bash


#variables
api_version=2020-12-01
source_endpoint=https://$source_workspace_name.dev.azuresynapse.net
target_endpoint=https://$workspace_name.dev.azuresynapse.net


# List artifact type and store in an array, removing spaces
#mapfile -t var_array < <(az synapse $aztype list --workspace-name $source_workspace_name --query "[].name" -o tsv | sed 's/ //g')
mapfile -t var_array < <((curl -s -X GET -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" $source_endpoint/$1s?api-version=$api_version | jq -r '.value[].name') | sed 's/ //g')

# Loop over the array to get each artifact type and save as .json file
for var in "${var_array[@]}"; 
do
    curl -X GET -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" https://$source_workspace_name.dev.azuresynapse.net/$1s/$var?api-version=$api_version > "${var}.json";
done

# Loop over the array and put each artifact type to target workspace.
for var in "${var_array[@]}"; 
do
	curl -X PUT -d @$var.json -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" https://$workspace_name.dev.azuresynapse.net/$1s/$var?api-version=$api_version;	
done

# Clean up
for var in "${var_array[@]}"; 
do
	rm $var.json;
done