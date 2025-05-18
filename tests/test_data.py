import pandas as pd

def test_data_exists():
    df = pd.read_csv("data/todays_games.csv")
    assert not df.empty, "Data is empty!"