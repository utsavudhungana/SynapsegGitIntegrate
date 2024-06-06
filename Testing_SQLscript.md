**Testing SQL Script import/export using REST API**

- I am using REST API documentation provided [here](https://learn.microsoft.com/en-us/rest/api/synapse/data-plane/sql-script/get-sql-script?view=rest-synapse-data-plane-2020-12-01&tabs=HTTP) by microsoft.
- Created SQL script called "SQLscript1" in the dev environment portal first. Then fetched the information using postman through GET api.
- Notice the response is straight forward showing current connection and pool name of serverless sql, in case of Dedicated SQL pool when deploying to another env parameter override is needed in case of different dedicated sql pool name.
  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/1da8fb8f-66de-40d0-9b17-8eca4870b8d4)

- Next, I created PUT request after adding json data from earlier pull. Here is the response I got.
  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/4934aa6f-9706-4085-8cf7-b3a1f1e6b1d3)

- SQLscript1 gets created in the target env with same content without any problem.
  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/f5c02d48-8936-4e21-9037-f66cb00d95a8)
