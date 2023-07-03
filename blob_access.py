import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

account_url = "https://amancloudtrainingstorage.blob.core.windows.net"
default_credential = DefaultAzureCredential()
container_name = "container1"

blob_service_client = BlobServiceClient(account_url, credential=default_credential)
local_path = "./data"
local_file_name

def download_blob():
    file_name = "folder1/temp.py"
    download_file_path = os.path.join(local_path, str.replace('DOWNLOAD.txt'))
    container_client = blob_service_client.get_container_client(container= container_name)
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(file=download_file_path, mode="wb") as download_file:
        download_file.write(container_client.download_blob().readall())


def write_blob():
     # Create a local directory to hold blob data
    os.mkdir(local_path)
    # Create a file in the local data directory to upload and download
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)

    # Write text to the file
    file = open(file=upload_file_path, mode='w')
    file.write("Hello, World!")
    file.close()

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

       # Upload the created file
    with open(file=upload_file_path, mode="rb") as data:
        blob_client.upload_blob(data)


try:
    download_blob()


except Exception as ex:
    print('Exception:')
    print(ex)
