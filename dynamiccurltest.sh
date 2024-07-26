#!/bin/bash


#variables
api_version=2020-12-01
source_endpoint=https://$source_workspace_name.dev.azuresynapse.net
target_endpoint=https://$workspace_name.dev.azuresynapse.net

if [[ $1 == "sqlScript" ]]; then
aztype="sql-script"
elif [[ $1 == "linkedservice" ]]; then
aztype="linked-service"
elif [[ $1 == "sparkJobDefinition" ]]; then
aztype="spark-job-definition"
else
aztype=$1
fi

# List artifact type and store in an array, removing spaces
mapfile -t var_array < <(az synapse $aztype list --workspace-name $source_workspace_name --query "[].name" -o tsv | sed 's/ //g')

# Loop over the array to get each artifact type and save as .json file
for var in "${var_array[@]}"; 
do
    curl -X GET -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" $source_endpoint/$1s/$var?api-version=$api_version > "${var}.json";
done

# Loop over the array and put each artifact type to target workspace.
for var in "${var_array[@]}"; 
do
	if [[ $1 == "linkedservice" && $var == "$source_workspace_name-WorkspaceDefaultSqlServer" ]] || [[ $1 == "linkedservice" && $var == "$source_workspace_name-WorkspaceDefaultStorage" ]]; then
	 continue
	else
		curl -X PUT -d @$var.json -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" $target_endpoint/$1s/$var?api-version=$api_version;	
	fi
done

# Clean up
for var in "${var_array[@]}"; 
do
	rm $var.json;
done
