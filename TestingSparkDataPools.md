**Testing Bit Data Pool Import/Export using API **
- We will be using API documented by microsoft [here](https://learn.microsoft.com/en-us/rest/api/synapse/resourcemanager/big-data-pools/create-or-update?view=rest-synapse-resourcemanager-2021-06-01-preview&tabs=HTTP).
- I have created "pool1" in dev environment from portal. Next I will use GET API to fetch pool1 information.
- use `` az login `` and `` az account get-access-token --resource=https://management.azure.com/ --query accessToken --output tsv `` to generate bearer token before sending request.
- I was able to fetch the data pool1 information successfully. Now, I will use same information and try to create pool in IT env.
  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/c26770ff-d1c6-4d2b-b09c-c9a7266ef670)

- Then, I used content from earlier, striped "id" property out, and sent a PUT request to target IT env. I was able to get 202 Accepted response.
  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/c3b4d9f9-6de7-4c83-812f-5471ef4bd269)
 
  In the IT env, pool1 is created successfully.
  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/785d6ed9-b04e-4d22-bcaa-8423737102aa)

- Now that we have pools getting created, what we can do is deploy all pools first -> then deploy notebooks -> then deploy pieplines. So that there will not be any problems.
