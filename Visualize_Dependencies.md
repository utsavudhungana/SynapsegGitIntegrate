- Install this module first

  `` $module = 'azure.synapse.tools'
    Install-Module $module -Scope CurrentUser ``

- Setup root folder of artifacts repository.

  ``$RootFolder = "x:repo\synapse"``

- Import and generate mermaid diagram, then save it as .md file.

  ``$synapse = Import-SynapseFromFolder -RootFolder $RootFolder -SynapseWorkspaceName 'whatever'
  Get-SynapseDocDiagram -synapse $synapse | Set-Content -Path 'synapse-diagram.md' ``

- Install this extension in VS Code. Then you will be able to visualize the diagram. Extension ID: bierner.markdown-mermaid

  ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/42468378-9105-4f31-99b9-0572a09b9575)

- Open .md file in VS Code and click this button to see preview.

   ![image](https://github.com/utsavudhungana/SynapsegGitIntegrate/assets/139304818/f793ea57-9d2f-4c00-81f9-872acad7c331)



