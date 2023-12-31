import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

account_url = "https://amancloudtrainingstorage.blob.core.windows.net"
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "container1"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container= container_name)
local_path = "./data"
local_file_name = ""

def download_blob():
    file_name = "folder1/temp.py"
    download_file_path = os.path.join(local_path, 'DOWNLOAD.txt')
    print("\nDownloading blob to \n\t" + download_file_path)

    with open(file=download_file_path, mode="wb") as download_file:
        download_file.write(container_client.download_blob(file_name).readall())


def list_containers():
    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        print("\t" + blob.name)


def write_blob():
    # Create a local directory to hold blob data
    # os.mkdir(local_path)
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
    list_containers()

except Exception as ex:
    print('Exception:')
    print(ex)
