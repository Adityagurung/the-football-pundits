from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
from google.api_core import exceptions

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Exports data to GCS with timeout handling and compression.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'capstone_datalake'
    object_key = 'raw/appearances.parquet'

    try:
        GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
            df,
            bucket_name,
            object_key,
            timeout=600  # 👈 10-minute timeout
        )
    except exceptions.GoogleAPICallError as e:
        print(f"GCS API Error: {e}")
    except exceptions.RetryError as e:
        print(f"Retry failed: {e}")