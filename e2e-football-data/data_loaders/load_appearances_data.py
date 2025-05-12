import io
import pandas as pd
import requests
import time

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API with retry logic
    """
    url = 'https://media.githubusercontent.com/media/abhirup-ghosh/e2e-data-pipeline/main/data/appearances.csv'

    appearance_dtype = {
        'appearance_id': str,
        'game_id': pd.Int64Dtype(),
        'player_id': pd.Int64Dtype(),
        'player_club_id': pd.Int64Dtype(),
        'player_current_club_id': pd.Int64Dtype(),
        'player_name': str,
        'competition_id': str,
        'yellow_cards': pd.Int64Dtype(),
        'red_cards': pd.Int64Dtype(),
        'goals': pd.Int64Dtype(),
        'assists': pd.Int64Dtype(),
        'minutes_played': pd.Int64Dtype()
    }

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            # Parse CSV text into DataFrame with your dtypes and date parsing
            return pd.read_csv(
                io.StringIO(resp.text),
                sep=',',
                dtype=appearance_dtype,
                parse_dates=['date'],
            )
        except requests.HTTPError:
            if attempt == max_retries:
                # let Mage log the final failure
                raise
            # exponential backoff before retrying
            time.sleep(2 ** attempt)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
