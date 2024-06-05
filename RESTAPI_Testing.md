# SynapseGitIntegrate

- Testing API get: Link to API documentation is [Here](https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/pipeline/get-pipeline?view=rest-synapse-data-plane-2020-12-01&tabs=HTTP)
- Created a synaspe workspace and turned up a pipeline that will run a notebook.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/bef6cac0-93f3-4639-a240-590db2f3040c)

- Next fetched pipeline using API from documentation above where I used Get to pull pipeline from synapse name "testpipeline1".

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/4ba27fee-9d6a-47c5-832c-9139a9856393)

- Now to deploy it to another synapse workspace I created another workspace in different resource group.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/aefb1846-c0ba-4651-b1eb-c19a7b9ef64f)

- Then I sent a PUT request to this new workspace after simply pasting content from the response I got earlier. This is what I got back.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/1171c0c4-7c51-418d-9e99-326942d0d8f5)

- Got an 202 Accepted response with state mentioned "Creating". Waited 5 min and refereshed synsapse studio. Pipeline was not created here.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/e6f5f6e7-5dbc-4b48-8459-524f214bf43f)

- Next I tried to send a PUT request after adding content from example in microsoft documentation. This is the response I got. [Link](https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/pipeline/create-or-update-pipeline?view=rest-synapse-data-plane-2020-12-01&tabs=HTTP#pipelines_create) to PUT request documentation.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/892a4cb5-c57d-4d54-a648-f74efd32f04b)

- Still no pipeline was created in workspace "gitsynapsetesting2it".

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/43f61e3c-ee9e-469b-8157-bb61ee2ead95)

- Now I tried to create. Here, postman response shows accepted and notebook created in synapse workspace. Though there is pre-requesite of having same spark pool already existing.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/71ab72e1-3dd6-4d55-a8f5-5fa4eb78b986)

- Here is the screenshot of new notebook created in IT environment. Note spark pool already attached to it. Also, output is also shown
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/d28ca75f-f88e-48c2-bb87-d662fe7fb1a6)


- Here are logs showing completed action.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/dc704f87-6b2f-4729-a3cc-ec0e8ec4f6bc)


![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/7dcfac20-1631-46bf-ad36-a4f5233825a7)

Logs can be found in root directory named query_data.csv
