source_workspace_name="synawsp-dev-1"
workspace_name="synawsp-dev-2"

# List Spark job definitions and store in an array, removing spaces
mapfile -t job_definition_array < <(az synapse spark-job-definition list --workspace-name $source_workspace_name --query "[].name" -o tsv | sed 's/ //g')

# Loop over the array to show each Spark job definition and save as .json file
for job_definition in "${job_definition_array[@]}"; 
do
    curl -X GET -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" https://$source_workspace_name.dev.azuresynapse.net/sparkJobDefinitions/$job_definition?api-version=2020-12-01 > "${job_definition}.json";
done

for job_definition in "${job_definition_array[@]}"; 
do
	curl -X PUT -d @$job_definition.json -H "Authorization: Bearer $(az account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output tsv)" https://$workspace_name.dev.azuresynapse.net/sparkJobDefinitions/$job_definition?api-version=2020-12-01;	
done

for job_definition in "${job_definition_array[@]}"; 
do
	rm $job_definition.json;	
done
