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

- Now I tried to create. Here, postman response shows accepted and notebook created in synapse workspace. Note: Spark Pool with same name needs to pre-exist in the target workspace.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/71ab72e1-3dd6-4d55-a8f5-5fa4eb78b986)

- Here is the screenshot of new notebook created in IT environment. Note spark pool already attached to it. Also, output is also shown in the notebook.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/99162f5f-95ee-49fc-b279-abfafc883b6d)


- Now, I created another notebook without attaching spark pool. Fetched the notebook details using GET api from postman, and sent a PUT request to IT enviroment using same content I got earlier. Note: pool is null here in this case.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/136bc9f2-f4d1-47d9-826d-d703ca60acd1)

- In this case, above case where bigdatapool is null notebook "test2notebook" is created without any problem. Note: No spark pool is attached here.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/d44254f0-c90d-4a26-a009-70f3b7f34111)

- Given that we have deployed both "test1notebook" and "test2notebook" notebook to IT env. Now, lets try to deploy testpipeline1 from "gitsynapsetesting" workspace to "gitsynapsetesting2it" that will run test1notebook notebook. Remember earlier pipeline was not created even though API response gave us green sign.

- Fetch testpipeline1 data using GET api.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/e2c76bce-ccd6-48f7-8462-9feeec5d20ae)

- Next, I copied the content from earlier step and sent PUT request to IT env. Note the reference to test1notebook here.

  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/daa9122e-2ea0-4933-ab87-c234b65e0e6a)
  
- Status shows accepted. and pipeline state shows "Updating". Note: It remembers previous deployment try even though the pipeline was not created for which no error was shown.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/7a66acea-d921-4abd-a015-d0d27961cd37)

- This time since test1notebook is present, pipeline is created in IT env.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/12aa5f06-e9a3-47b6-9972-8464d4f5c357)

- Lets, try to deploy testpipeline2 that has test2notebook attached with no spark pool configured within notebook. Here, I repeat same process as above, only changing name. This time it shows creating state when sending PUT request.

  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/abb73219-ee97-4f7e-9fa7-4f480d1da4df)

- testpipeline2 created in IT env without any problem now.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/48702cb0-ac4a-41df-a895-1305ee694a67)

- I will now create third "test3notebook" notebook in dev env attach spark pool "poo2" after creating it, create another pipeline "testpipeline3" with notebook "test3notebook" and try to deploy to IT env that does not have "pool2" yet. Here I follow same process as earlier, first fetch using GET, copy reponse body, paste it in PUT request body and change workspace and pipeline name in the request.

- Note: It is refering to test3notebook here.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/3954bbb7-3985-47c8-8d53-2faf94a900a9)

  Creating state with accepted status.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/9d85904d-8c0d-4da4-a950-2428a8974566)

And the pipeline is not created since its missing test3notebook that it is referring to. Next I created "test3notebook" thorugh portal without "pool2" since its not yet created in IT env. Then I ran pipeline3 PUT request again.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/eccd517b-3b65-48e4-becb-6eef94f91c30)

- Now in this case, where I created test3notebook manually(did manual because RESTAPI can create without preexisting spark or override spark name) in IT env without attaching spark, then deployed pipeline3 it worked.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/3dd148df-f3dd-48e3-80cf-6f0d4d207fb0)



- Here are some screenshot of logs showing completed action. Note: It does not give any error response even when notebook is not created.

![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/dc704f87-6b2f-4729-a3cc-ec0e8ec4f6bc)


![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/7dcfac20-1631-46bf-ad36-a4f5233825a7)

Logs can be found in root directory named query_data.csv
