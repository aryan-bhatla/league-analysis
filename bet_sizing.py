#----------------------------------------------------------------------------------------------------- # 
# Bet based on Kelly Criterion
#----------------------------------------------------------------------------------------------------- # 
def kelly_bet(calculated_win_prob: float, odds_your_team: float, odds_other_team: float) -> float: 
    '''
        
        Parameters: 
            calculated_win_prob (float): Winrate you have calculated for a team
            odds_your_team (float): Bookmaker odds for team you are betting on
            odds_other_team (float): Bookmaker odds for team you are not betting on
            
        Returns: 
            bet_size (float): Maximum bet size calculated via Kelly criterion 

    '''
    # Calculate win probability that bookmaker has determined 
    implied_win_prob = odds_your_team / (odds_your_team + odds_other_team) 

    # Set-up Kelly equation
    numerator = (odds_your_team * calculated_win_prob) - implied_win_prob 

    # Derive maximal bet size 
    bet_size = numerator / odds_your_team

    return bet_size 