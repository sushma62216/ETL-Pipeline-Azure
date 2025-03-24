import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient

# Load .env file
load_dotenv()

# Read the connection string from environment variables
AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
container_name="container-name"
blob_name="blob-name"
local_file_path="weather_data.json"

def upload_to_blob():
    blob_service_client=BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    blob_client=blob_service_client.get_blob_client(container=container_name,blob=blob_name)

    with open(local_file_path, 'rb') as data:
        blob_client.upload_blob(data,overwrite=True)

    print(f"Uploaded {blob_name} to Azure Blob Storage")

if __name__=="__main__":
    upload_to_blob()
