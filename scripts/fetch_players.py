from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd

def fetch_top_scorers():
    players_stats = leaguedashplayerstats.LeagueDashPlayerStats().get_data_frames()[0]

    #sort players by pts and keep only the top 100
    top_scorers = players_stats.sort_values(by='PTS', ascending=False).head(100)
    
    top_scorers.to_csv("data/top_scorers.csv", index=False)
    print(top_scorers)
    return top_scorers

if __name__ == "__main__":
    fetch_top_scorers()