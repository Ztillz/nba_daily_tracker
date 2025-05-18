from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

def fetch_today_games():
    games = scoreboard.ScoreBoard().games.get_dict()
    df = pd.DataFrame(games)
    df.to_csv("data/todays_games.csv", index=False)
    return df


if __name__ == "__main__":
    fetch_today_games()