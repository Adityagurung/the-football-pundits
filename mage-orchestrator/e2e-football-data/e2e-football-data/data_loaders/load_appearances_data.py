import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load and filter appearance data from GitHub
    """
    url = 'https://media.githubusercontent.com/media/abhirup-ghosh/e2e-data-pipeline/main/data/appearances.csv'
    
    # Define data types with optimized pandas dtypes
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
        'minutes_played': pd.Int64Dtype(),
    }

    # Columns to keep in final dataset
    cols_to_use = [
        'player_id', 'date', 'player_name', 'competition_id',
        'yellow_cards', 'red_cards', 'goals', 'assists', 'minutes_played',
        'name', 'sub_type', 'type', 'country_name'
    ]

    # Load data with type conversions
    df = pd.read_csv(
        url,
        sep=',',
        dtype=appearance_dtype,
        parse_dates=['date'],
        usecols=cols_to_use + ['date']  # Ensure we load date for parsing
    )
    
    # Filter columns first
    df = df[cols_to_use]
    
    # Apply business logic filters
    df = df[
        (df['type'] == 'domestic_league') & 
        (df['sub_type'] == 'first_tier')
    ]
    
    # Filter for top 5 European leagues
    countries_to_keep = ['England', 'Spain', 'Germany', 'Italy', 'France']
    df = df[df['country_name'].isin(countries_to_keep)]
    
    return df

@test
def test_output(output, *args) -> None:
    """
    Validation tests for the data output
    """
    assert output is not None, 'The output is undefined'
    assert not output.empty, 'The output DataFrame is empty'
    assert set(output['country_name'].unique()).issubset(
        {'England', 'Spain', 'Germany', 'Italy', 'France'}
    ), 'Invalid countries found'
    assert (output['type'] == 'domestic_league').all(), 'Invalid competition type'
    assert (output['sub_type'] == 'first_tier').all(), 'Invalid competition sub-type'