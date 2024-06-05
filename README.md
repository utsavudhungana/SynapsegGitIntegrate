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

- Got an 202 Accepted response with state mentioned "Updating". Waited 5 min and refereshed synsapse studio. Pipeline was not created here.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/e6f5f6e7-5dbc-4b48-8459-524f214bf43f)

- Next I tried to send a PUT request after adding content from example in microsoft documentation. This is the response I got.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/892a4cb5-c57d-4d54-a648-f74efd32f04b)

- Still no pipeline was created.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/43f61e3c-ee9e-469b-8157-bb61ee2ead95)

