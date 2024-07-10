import os
import requests
import gitlab
import argparse
from azure.cli.core import get_default_cli

def get_file_paths_from_gitlab_directory(repo_id, directory_path, ref, gitlab_url, private_token):
    gl = gitlab.Gitlab(gitlab_url, private_token=private_token, api_version=4)
    project = gl.projects.get(repo_id)
    files = project.repository_tree(path=directory_path, ref=ref, all=True)
    file_paths = [file['path'] for file in files if file['type'] == 'blob']
    return file_paths

def get_file_content_from_gitlab(repo_id, file_path, ref, gitlab_url, private_token):
    gl = gitlab.Gitlab(gitlab_url, private_token=private_token)
    project = gl.projects.get(repo_id)
    file = project.files.get(file_path=file_path, ref=ref)
    return file.decode().decode()

def send_put_request(url, headers, body_content):
    response = requests.put(url, headers=headers, data=body_content)
    return response.status_code, response.text

def construct_api_url(base_url, file_path, artifact_type):
    # Extract the file name without the extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    
    # Construct the URL with the file name as a parameter
    return f'{base_url}/{artifact_type}/{file_name}?api-version=2020-12-01'

def az_cli(args_str):
    args = args_str.split()
    cli = get_default_cli()
    cli.invoke(args)
    if cli.result.result:
        return cli.result.result
    elif cli.result.error:
        raise cli.result.error
    return True

def main(repo_id, ref, target_workspace_name, artifact_type, directory_path):
    # GitLab configuration
    gitlab_url = 'https://gitlab.com'  # Your GitLab instance URL
    private_token = os.getenv('GITLAB_PRIVATE_TOKEN')  # Ensure you set this environment variable

    # Fetch Bearer token
    API_TOKEN = az_cli("account get-access-token --resource=https://dev.azuresynapse.net/ --query accessToken --output none")

    # REST API configuration
    base_api_url = f'https://{target_workspace_name}.dev.azuresynapse.net'  # Base URL for the API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_TOKEN
    }
    
    # Get list of files in the directory
    try:
        file_paths = get_file_paths_from_gitlab_directory(repo_id, directory_path, ref, gitlab_url, private_token)
    except Exception as e:
        print(f'Failed to retrieve file paths from directory: {e}')
        return

    for file_path in file_paths:
        try:
            body_content = get_file_content_from_gitlab(repo_id, file_path, ref, gitlab_url, private_token)
            api_url = construct_api_url(base_api_url, file_path, artifact_type)
            status_code, response_text = send_put_request(api_url, headers, body_content)
            
            print(f'Successfully processed {file_path} with status code {status_code}')
            print(response_text)
        except Exception as e:
            print(f'Failed to process {file_path}: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some parameters.')
    parser.add_argument('--repo_id', type=str, required=True, help='The ID of the GitLab repository.')
    parser.add_argument('--ref', type=str, required=True, help='The branch name or commit hash.')
    parser.add_argument('--target_workspace_name', type=str, required=True, help='The name of the Synapse workspace.')
    parser.add_argument('--artifact_type', type=str, required=True, help='The type of artifacts to publish.')
    parser.add_argument('--directory_path', type=str, required=True, help='The path of the directory in the GitLab repository.')

    args = parser.parse_args()

    main(args.repo_id, args.ref, args.target_workspace_name, args.artifact_type, args.directory_path)