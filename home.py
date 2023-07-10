import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from flask import Flask

account_url = "https://amancloudtrainingstorage.blob.core.windows.net"
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "container1"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container= container_name)
local_path = "./data"
local_file_name = ""


def list_containers():
    print("\nListing blobs...")

    # List the blobs in the container
    blob_list = container_client.list_blobs()
    return blob_list


app = Flask(__name__)

@app.route("/")
def home():
    items = list_containers()
    head_html = "<h2>Azure Storage account Blob SDK!</h2>"
    blob_lst_html = "\n".join(["<h4>" + blob_name + "</h4>" for blob_name in items])
    return head_html + blob_lst_html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)