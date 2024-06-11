::: mermaid
graph LR
linkedService.gitsynapsetesting-WorkspaceDefaultSqlServer --> integrationRuntime.AutoResolveIntegrationRuntime
linkedService.gitsynapsetesting-WorkspaceDefaultStorage --> integrationRuntime.AutoResolveIntegrationRuntime
pipeline.pipeline1 --> notebook.Notebook_1
dataset.dataset1 --> linkedService.gitsynapsetesting-WorkspaceDefaultStorage 
sparkJobDefinition.Spark_job_definition_1 --> bigDataPool.pool1
:::
