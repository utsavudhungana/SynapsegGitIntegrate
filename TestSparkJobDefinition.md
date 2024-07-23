- Created couple of spark definition with file path to a python script and attached small spark pool to it.
![image](https://github.com/user-attachments/assets/de7f32c5-f45e-4922-a828-65739f2e44ac)

- Then listed the spark definition using this az command.
   ```
    source_workspace_name="testsynapseworkspace"
    workspace_name="targetworkspacename"
    az synapse spark-job-definition list --workspace-name $workspace_name --query "[].name" -o tsv
  ```
- Stored the list in an array in bash then used loop to get spark job definition content and store as json file.
  ```
   mapfile -t job_definition_array < <(az synapse spark-job-definition list --workspace-name $source_workspace_name --query "[].name" -o tsv | sed 's/ //g')
  ```
  ```
  for job_definition in "${job_definition_array[@]}"; do az synapse spark-job-definition show --workspace-name $source_workspace_name --name "$job_definition" > "${job_definition}.json"; done
  ``` 
- Next tried to create the spark definition in target workspace using this command.
   ```
   for f in *.json; do job_definition_name=$(basename $f | cut -f 1 -d '.'); az synapse spark-job-definition create --workspace-name synawsp-dev-2 --name "$job_definition_name" --file @"$f"; done;
   ``` 
- It failed at first as the spark pool referenced in the definition was not already deployed in target workspace. Hence created the spark pool manually for the testing in target workspace and tried again.
  ![image](https://github.com/user-attachments/assets/4c66569a-e2e1-4a00-a5a8-2d702dbc2dea)

- Here is the proof of spark definition file deployed in target workspace i.e workspace ending with name dev-2.
  ![image](https://github.com/user-attachments/assets/0adcd6b7-0b30-4536-aba8-13887dea9d1f)
  
  ![image](https://github.com/user-attachments/assets/04e70585-37f6-4fef-974b-b63c674d802e)

-Notice the problem here. Spark pool and file path are not imported properly even though its deployed in target workspace.


**TEST 2:**

-Removed earlier definition files and created two new spark job definitions in dev.
![image](https://github.com/user-attachments/assets/ee193416-5c91-4dba-9908-7d7211c1b2d7)

-Ran script commands one by one.
![image](https://github.com/user-attachments/assets/ece23d0a-39d4-40d0-9683-8574f555d74c)

-Got successful response back from command. 
![image](https://github.com/user-attachments/assets/a9ad2bdd-b64a-4052-b6fe-2148dea46139)

-Still spark pool is not attached properly.
![image](https://github.com/user-attachments/assets/73681958-2d39-4f51-9691-ad45dd455187)

-Even though file path and target spark pool is mentioned in json file to be imported. It is not correctly getting attached after import though same pool name is present is both workspace.

![image](https://github.com/user-attachments/assets/f2003371-ebb1-47e6-b69d-bacd0eaf3750)

![image](https://github.com/user-attachments/assets/8049415f-28e8-4c48-9c7e-49c7f8440897)

-Tried just by showing and importing only one spark definition file as well but same outcome. No luck.

![image](https://github.com/user-attachments/assets/76040c28-07ad-4e7f-ad77-4b8f2a8e49c1)

![image](https://github.com/user-attachments/assets/5d8c8386-a60a-4aa2-bf01-33dced15caf5)

-Screeshot of spark pool with same name in both workspace.

![image](https://github.com/user-attachments/assets/316c314c-72c5-4f46-af42-2abe3aa9a1cd)

![image](https://github.com/user-attachments/assets/39b02e25-3564-4583-9f0c-04cd1f66edd9)

- This proves that Spark Job definition export and import using az cli cannot import all configuration and content of the object.
