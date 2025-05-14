from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
# no longer import GoogleCloudStorage here
from pandas import DataFrame
from os import path
from google.cloud import storage
import io

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Exports a DataFrame as Parquet to GCS using manual upload
    with controlled chunk size and explicit timeout.
    """
    # 1. Prepare in-memory Parquet
    buffer = io.BytesIO()
    df.to_parquet(buffer, index=False)
    buffer.seek(0)

    # 2. Initialize GCS client and blob
    client = storage.Client()                                    # standard client :contentReference[oaicite:3]{index=3}
    bucket = client.bucket('capstone_datalake')
    blob = bucket.blob('raw/appearances.parquet')

    # 3. Lower chunk size to 5 MiB to keep each RPC fast
    blob.chunk_size = 5 * 1024 * 1024                           # must be multiple of 256 KiB :contentReference[oaicite:4]{index=4}

    # 4. Upload with a 10‑minute timeout
    try:
        blob.upload_from_file(
            buffer,
            content_type='text/plain',
            timeout=600                                         # supported here :contentReference[oaicite:5]{index=5}
        )
    except Exception as e:
        print(f"Upload failed: {e}")
