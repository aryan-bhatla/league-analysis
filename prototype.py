#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import glob
import helper_functions as helpers
import numpy as np 
import os 
import pandas as pd
import prototype 
import scipy 
import sklearn 

#----------------------------------------------------------------------------------------------------- # 
# Data preparation
#----------------------------------------------------------------------------------------------------- # 
def prepare_data(pathname: str, *additional_pathname: str) -> pd.DataFrame:
    '''
        
        Parameters: 
            pathname (str): Folder containing statistics for different regions/events

        Optional Parameters: 
            additional_pathname (str): Additional folders containing statistics for different regions/events
        
        Returns: 
            final_data (pd.DataFrame): Cleaned and averaged statistics
    
    '''
    # List to hold all DataFrames
    dataframes = []

    # Iterate over the initial pathname and any additional pathnames
    for directory in [pathname, *additional_pathname]:
        
        # Construct the full file path for each file in the directory
        for file_path in glob.glob(os.path.join(directory, '*.csv')): 
            
            # Read the file and append to the list of DataFrames
            df = pd.read_csv(file_path)
            dataframes.append(df)

    # Concatenate all data together
    joined_data = pd.concat(dataframes, ignore_index=True)

    # Clean initial data 
    cleaned_data = helpers.cleanup_data(joined_data)
    
    # Collect total stats across each split 
    appended_data = helpers.append_data(cleaned_data)

    # Sum player stats across splits
    summed_data = helpers.sum_data(appended_data)

    # Average and re-clean data 
    final_data = helpers.average_data(summed_data)

    return final_data


# #----------------------------------------------------------------------------------------------------- # 
# # Elo calculation
# #----------------------------------------------------------------------------------------------------- # 
# # Elo rating formula (equal weightings for now)
# def calc_player_elo(param_dct: dict) -> int: 
#     '''
    
#         Parameters: 
#             param_dct (dict): Statistics of given player 
        
#         Returns: 
#             elo (int): Calculated elo of given player

#     '''
#     return elo