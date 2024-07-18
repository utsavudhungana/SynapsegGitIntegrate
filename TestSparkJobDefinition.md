- Created couple of spark definition with file path to a python script and attached small spark pool to it.\
![image](https://github.com/user-attachments/assets/de7f32c5-f45e-4922-a828-65739f2e44ac)

- Then listed the the spark definition this az command.\
   ```
    source_workspace_name="testsynapseworkspace"
    workspace_name="targetworkspacename"
    az synapse spark-job-definition list --workspace-name $workspace_name --query "[].name" -o tsv
  ```
- Stored the list in an array in bash then used loop to get spark job definition content and store as json file.\
  ```mapfile -t job_definition_array < <(az synapse spark-job-definition list --workspace-name $source_workspace_name --query "[].name" -o tsv | sed 's/ //g')```
  ```for job_definition in "${job_definition_array[@]}"; do az synapse spark-job-definition show --workspace-name $source_workspace_name --name "$job_definition" > "${job_definition}.json"; done ``` \
- Next tried to create the spark definition in target workspace using this command.\
   ```
   for f in *.json; do job_definition_name=$(basename $f | cut -f 1 -d '.'); az synapse spark-job-definition create --workspace-name synawsp-dev-2 --name "$job_definition_name" --file @"$f"; done;
   ``` \
- It failed at first as the spark pool referenced in the definition was not already deployed in target workspace. Hence created the spark pool manually for the testing in target workspace and tried again.\ 
  ![image](https://github.com/user-attachments/assets/4c66569a-e2e1-4a00-a5a8-2d702dbc2dea)

- Here is the proof of spark definition file deployed in target workspace i.e workspace ending with name dev-2.\
  ![image](https://github.com/user-attachments/assets/0adcd6b7-0b30-4536-aba8-13887dea9d1f)
  
  ![image](https://github.com/user-attachments/assets/04e70585-37f6-4fef-974b-b63c674d802e)

-Notice the problem here. Spark pool and file path are not imported properly even though its deployed in target workspace.
 
