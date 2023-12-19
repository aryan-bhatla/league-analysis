#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import numpy as np 
import pandas as pd 
import scipy 
import sklearn 
import helper_functions as helpers


#----------------------------------------------------------------------------------------------------- # 
# Data collection 
#----------------------------------------------------------------------------------------------------- # 
# 2022 Spring Regular Season 
twenty_two_spring_regular = pd.read_csv('LCK_Player_Data/2022 Spring.csv')
twenty_two_spring_regular.reset_index(drop=True, inplace=True)

# 2022 Spring Playoffs
twenty_two_spring_playoff = pd.read_csv('LCK_Player_Data/2022 Spring Playoffs.csv')
twenty_two_spring_playoff.reset_index(drop=True, inplace=True)

# 2022 Summer Regular Season 
twenty_two_summer_regular = pd.read_csv('LCK_Player_Data/2022 Summer.csv')
twenty_two_summer_regular.reset_index(drop=True, inplace=True)

# 2022 Summer Playoffs
twenty_two_summer_playoff = pd.read_csv('LCK_Player_Data/2022 Summer Playoffs.csv')
twenty_two_summer_playoff.reset_index(drop=True, inplace=True)

# 2023 Spring Regular Season 
twenty_three_spring_regular = pd.read_csv('LCK_Player_Data/2023 Spring.csv')
twenty_three_spring_regular.reset_index(drop=True, inplace=True)

# 2023 Spring Playoffs
twenty_three_spring_playoff = pd.read_csv('LCK_Player_Data/2023 Spring Playoffs.csv')
twenty_three_spring_playoff.reset_index(drop=True, inplace=True)

# 2023 Summer Regular Season 
twenty_three_summer_regular = pd.read_csv('LCK_Player_Data/2023 Summer.csv')
twenty_three_summer_regular.reset_index(drop=True, inplace=True)

# 2023 Summer Playoffs
twenty_three_summer_playoff = pd.read_csv('LCK_Player_Data/2023 Summer Playoffs.csv')
twenty_three_summer_playoff.reset_index(drop=True, inplace=True)


#----------------------------------------------------------------------------------------------------- # 
# Data preparation
#----------------------------------------------------------------------------------------------------- # 
def prepare_data(df1: pd.DataFrame, df2: pd.DataFrame, df3: pd.DataFrame, df4: pd.DataFrame, 
                 df5: pd.DataFrame, df6: pd.DataFrame, df7: pd.DataFrame, df8: pd.DataFrame) -> pd.DataFrame:
    '''
        
        Parameters: 
            df1-df8 (pd.DataFrame): Statistics from Spring Regular Season 2022 - Summer Playoffs 2023 
        
        Returns: 
            final_data (pd.DataFrame): Cleaned and averaged statistics
    
    '''
    # Combine all data sources 
    joined_data = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8])

    # Clean initial data 
    cleaned_data = helpers.cleanup_data(joined_data)
    
    # Collect total stats across each split 
    appended_data = helpers.append_data(cleaned_data)

    # Sum player stats across splits
    summed_data = helpers.sum_data(appended_data)

    # Average and re-clean data 
    final_data = helpers.average_data(summed_data)

    return final_data


#----------------------------------------------------------------------------------------------------- # 
# Elo calculation
#----------------------------------------------------------------------------------------------------- # 
# Elo rating formula (equal weightings for now)
def calc_player_elo(param_dct: dict) -> int: 
    '''
    
        Parameters: 
            param_dct (dict): Statistics of given player 
        
        Returns: 
            elo (int): Calculated elo of given player

    '''
    return elo