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
    Template for loading data from API
    """
    url = 'https://media.githubusercontent.com/Adityagurung/the-football-pundits/main/data/competitions.csv'

    comp_dtype = {
        'competition_id': str,
        'competition_code': str,
        'name': str,
        'sub_type': str,
        'type': str,
        'country_id': pd.Int64Dtype(),
        'country_name': str,
        'domestic_league_code': str,
        'confederation': str,
        'url': str,
        'is_major_national_league': pd.Int64Dtype()
    }

    # ─── Replace this simple read_csv call ───────────────────────────────
    # return pd.read_csv(url, sep=',')
    #
    # ─── With the robust fetch-and-parse loop below ──────────────────────

    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            # parse the CSV text into a DataFrame
            return pd.read_csv(io.StringIO(resp.text), sep=',', dtype=comp_dtype)
        except requests.HTTPError:
            if attempt == max_retries:
                # on final failure, let Mage log and bubble up
                raise
            # otherwise wait exponentially longer each retry
            time.sleep(2 ** attempt)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
