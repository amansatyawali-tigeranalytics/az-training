import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

account_url = "https://amancloudtrainingstorage.blob.core.windows.net"
default_credential = DefaultAzureCredential()

blob_service_client = BlobServiceClient(account_url, credential=default_credential)

try:
    print("Azure Blob Storage Python quickstart sample")

                # Quickstart code goes here
except Exception as ex:
    print('Exception:')
    print(ex)
