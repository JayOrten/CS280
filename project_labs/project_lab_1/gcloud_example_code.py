from google.cloud import storage
from gcsfs import GCSFileSystem
import os
import pandas as pd

#If you need to iniate your service account environment variable, you can do it here, if you've already initiated it, you can skip this step
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/<your account name here>/airflow-cs280/auth/bucket_auth.json"

# Read the file from the bucket using the GCSFileSystem
fs = GCSFileSystem(project="<your gcp project name>")
with fs.open('gs://<your bucket name>/...pathtocsv/my_dataframe.csv', 'rb') as f:
    my_df = pd.read_csv(f)

# Upload the file to google cloud storage using the gcp client
# Initiate Client
client = storage.Client()
# Create a bucket object
bucket = client.get_bucket('<your bucket name>')

#Upload your df to the bucket
bucket.blob('...pathtocsv/my_dataframe.csv').upload_from_string(my_df.to_csv(index=False), 'text/csv')


