**Testing datasets import/export from one workspace to another**

- First I created dataset called "Dataset1" manually in dev environment. Then, sent GET request using [this](https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/dataset/create-or-update-dataset?view=rest-synapse-data-plane-2020-12-01&tabs=HTTP) api from microsoft documentation.
- GET request goes fine in this case. Now, I copy the content from here and create a PUT request to another workspace in IT.
  
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/9ff4c530-2490-4398-a4ce-1c9dc6bda6fe)

- PUT request goes through and a green sign with "Creating" state.

  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/e7d0649e-95c1-4e3b-ba4e-8b659e6c6867)

- But, data set is not created since it has reference to linked services and file which is not there in target workspace.

  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/a8351415-ee9e-4791-9488-57a5fa41182b)

- Lets try to create change linked service name to datalake storage name of target workspace. I changed "gitsynapsetesting-WorkspaceDefaultStorage" to  "gitsynapsetesting2it-WorkspaceDefaultStorage" in referenceName under linkedServiceName and sent PUT request again.

 ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/b157375e-4f60-448a-b2fb-d59e5cda6c03)

- I got updating state and this time dataset named "Dataset1" gets created in target workspace.

  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/30e38611-ea55-4679-ad0d-dab88c92c0e5)

- In this testing we found that linkedservice is one of the dependency of datasets i.e linkedservice need to pre-exits. Override parameter is also required here.




