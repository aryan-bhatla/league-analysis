#----------------------------------------------------------------------------------------------------- # 
# Logistics function 
#----------------------------------------------------------------------------------------------------- # 
def winrate_to_odds(team_one_winrate: float, team_two_winrate: float) -> list[float]:
    '''
        
        Parameters: 
            team_one_winrate, team_two_winrate (float): Team winrates against each other, should total 100% = 1

        Returns: 
            odds (list): Implied odds for each team based on their winrates

    '''
    # Final odds 
    odds_one = 100 / team_one_winrate 
    odds_two = 100 / team_two_winrate
    odds = [odds_one, odds_two]

    return odds 
