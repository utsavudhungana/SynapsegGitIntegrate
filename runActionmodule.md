Setup: To test gitaction locally.
Install:
```
npm i -g @github/local-action
```

Command to run:
```
local-action run ./ build_and_deploy/main.ts .env
```

Put all in root:
Need 2 template files
one override param file
one .env file. use example below: 

```
# Do not commit your actual .env file to Git! This may contain secrets or other
# private information.

# Enable/disable step debug logging (default: `false`). For local debugging, it
# may be useful to set it to `true`.
ACTIONS_STEP_DEBUG=true

# GitHub Actions inputs should follow `INPUT_<name>` format (case-insensitive).
INPUT_TargetWorkspaceName='targetWorkspace'
INPUT_TemplateFile='./TemplateForWorkspace.json'
INPUT_ParametersFile='./TemplateParametersForWorkspace.json'
INPUT_OverrideArmParameters='./it_parameters.yaml'
INPUT_environment='Azure Public'
INPUT_resourceGroup='rg-name'
INPUT_clientId=""
INPUT_clientSecret=""
INPUT_subscriptionId= ""
INPUT_tenantID=""
INPUT_operation= 'deploy'

# GitHub Actions default environment variables. These are set for every run of a
# workflow and can be used in your actions. Setting the value here will override
# any value set by the local-action tool.
# https://docs.github.com/en/actions/learn-github-actions/variables#default-environment-variables

# CI="true"
# GITHUB_ACTION=""
# GITHUB_ACTION_PATH=""
# GITHUB_ACTION_REPOSITORY=""
# GITHUB_ACTIONS=""
# GITHUB_ACTOR="mona"
# GITHUB_ACTOR_ID="123456789"
# GITHUB_API_URL=""
# GITHUB_BASE_REF=""
# GITHUB_ENV=""
# GITHUB_EVENT_NAME=""
# GITHUB_EVENT_PATH=""
# GITHUB_GRAPHQL_URL=""
# GITHUB_HEAD_REF=""
# GITHUB_JOB=""
# GITHUB_OUTPUT=""
# GITHUB_PATH=""
# GITHUB_REF=""
# GITHUB_REF_NAME=""
# GITHUB_REF_PROTECTED=""
# GITHUB_REF_TYPE=""
# GITHUB_REPOSITORY=""
# GITHUB_REPOSITORY_ID=""
# GITHUB_REPOSITORY_OWNER=""
# GITHUB_REPOSITORY_OWNER_ID=""
# GITHUB_RETENTION_DAYS=""
# GITHUB_RUN_ATTEMPT=""
# GITHUB_RUN_ID=""
# GITHUB_RUN_NUMBER=""
# GITHUB_SERVER_URL=""
# GITHUB_SHA=""
# GITHUB_STEP_SUMMARY=""
# GITHUB_TRIGGERING_ACTOR=""
# GITHUB_WORKFLOW=""
# GITHUB_WORKFLOW_REF=""
# GITHUB_WORKFLOW_SHA=""
# GITHUB_WORKSPACE=""
# RUNNER_ARCH=""
# RUNNER_DEBUG=""
# RUNNER_NAME=""
# RUNNER_OS=""
# RUNNER_TEMP=""
# RUNNER_TOOL_CACHE=""
```

Add this code at the end of main.ts

```
// Export 'run' so GitHub can call it
export async function run() {
    try {
        await main();  // Call the main logic inside run
    } catch (error) {
        console.error(error);
        process.exit(1);  // Exit with an error code
    }
}
```
