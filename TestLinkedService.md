**Testing LinkedService import/export using REST API**
- I am using api documentation provided [here](https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/linked-service/create-or-update-linked-service?view=rest-synapse-data-plane-2020-12-01&tabs=HTTP) by microsoft.
- First, I created linked service to data lake storage manually from portal. Here, I fetch the linked service information through GET request.
- Notice the name of linked service and url of the data lake storage here.
  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/d8af14cc-4a9d-4629-b192-6a50ad099b17)

- Next, I will create a PUT request using the content I got earlier. I replaced datalakestorage name to match target environment datalake storage name and sent the request. Below is the response.

  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/57779cc7-38a1-47f2-a7da-9a5091d03334)

- Linked service gets created in the IT env with the name same as source environment "AzureDataLakeStorage1" but then its connected to the datalake storage "devteststoragesynap2it" instead of "devdevteststoragesynap".
  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/661e0994-c1d2-4501-85da-3bf9141c1e52)

- Here we can see that linked service can be exported and imported easily using REST API but with the dependency of preexisting resource already available in target env. For example data lake storage.
  

  
