**Testing Bit Data Pool Import/Export using API **
- We will be using API documented by microsoft [here](https://learn.microsoft.com/en-us/rest/api/synapse/resourcemanager/big-data-pools/create-or-update?view=rest-synapse-resourcemanager-2021-06-01-preview&tabs=HTTP).
- I have created "pool1" in dev environment from portal. Next I will use GET API to fetch pool1 information.
- use ``` az login ``` and `` az account get-access-token --resource=https://management.azure.com/ --query accessToken --output tsv `` to generate bearer token before sending request.
- 
