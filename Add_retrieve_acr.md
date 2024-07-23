- Pre-requisite: Create Container Registry in Azure within your resource group. Az Cli and Docker Cli is needed. 
- Created [this](push_dir.sh) shell script which will push the content of a specified directly as docker image to container registry.
- Make sure to get access to container regirstry before running the script. Run the script with this values:  
![image](https://github.com/user-attachments/assets/b5d1afa1-404d-4317-b862-4925b3de93ed)

- Once the script finishes this is the message I got:
![image](https://github.com/user-attachments/assets/455f65ea-ba83-4857-854c-f5c4f3c584a8)

- Checked in my container registry to verify and here it is bravo!!:
![image](https://github.com/user-attachments/assets/9dff2ceb-9120-45db-b536-6110486fa18b)

- Next up created [this](pull_dir.sh) shell script to pull the image from the registry run it in docker container and copy its data to the current system in a directory.
  
- Ran it with below values:
![image](https://github.com/user-attachments/assets/56c765a6-eea4-4292-be62-0903d7d24613)

-Got this message at the end, checked my local directory and there it is all the content from previously pushed directory inside Extracted directory.

![image](https://github.com/user-attachments/assets/85eeb37b-66a2-433c-9c3d-227465b978a1)

![image](https://github.com/user-attachments/assets/d31944a7-5f42-4936-864c-1a860788c0bb)

- Tested and working
