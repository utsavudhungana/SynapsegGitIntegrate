We have two synapse workspace in same resourcegroup synawsp-dev1 and synawsp-dev2.
Added couple of pipleine in dev1 workspace.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/fd2e4433-ce9d-4de8-bcf0-21a4193e8f71)

And dev2 doesnot have any pipeline as of now.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/bbfbeff6-f81c-48e3-8060-235f388ebe3b)

Now I am running the sync_synapse_pipelin.py script with following arguments:
```python sync_synapse_pipeline.py --source_workspace_name synawsp-dev-1 --target_workspace_name synawsp-dev-2```

I was not able to run the code at first as I had not assigned contributor role in studio level of synapse after I added that role to the SP in both workspace I was able to easily run the code.
Once I run it I got bad request error. Good thing is we are getting error response when using python sdk. Error was point that notebooks are missing which are dependency to these pipelines.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/eab46f34-b89b-445a-948b-d8379de1eefb)

Next, I added these notebook manually from studio then run the code again. In reality we have to import notebooks/all dependecy artifacts first then run the code to import pipelines.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/a76783ce-0519-4c16-86a4-1afcb1c96927)

This time the program ran successfully and gave response back with this json result.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/efc79639-5834-4fa1-a09d-833a3e922ba9)

Both pipelines are created as well in target workspace with respective notebooks attached to them.
![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/be71e284-c532-4a7d-8cd9-4ab4ed331294)
