#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import data_preparation 
import models
import pandas as pd

from tqdm import tqdm


#----------------------------------------------------------------------------------------------------- # 
# Data preprocessing
#----------------------------------------------------------------------------------------------------- # 
# Load data 
final_data = data_preparation.prepare_data("LCK_Player_Data",
                                           "LCS_Player_Data",
                                           "LEC_Player_Data",
                                           "MSI_Player_Data",
                                           "Worlds_Player_Data")

# Clean up final row containing NaN
final_data.drop(final_data.tail(1).index, inplace = True)

# Split data into different roles 
grouped_data = final_data.groupby('Pos')

Support_data = grouped_data.get_group('Support')
ADC_data = grouped_data.get_group('ADC')
Middle_data = grouped_data.get_group('Middle')
Jungle_data = grouped_data.get_group('Jungle')
Top_data = grouped_data.get_group('Top')


#----------------------------------------------------------------------------------------------------- # 
# Results setup
#----------------------------------------------------------------------------------------------------- # 
# Number of iterations
num_iterations = 3

# Initialize a dictionary to store results for each iteration
all_results = {i: pd.DataFrame() for i in range(num_iterations)}

# Define roles
roles = ['Support', 'ADC', 'Middle', 'Jungle', 'Top']

# Initialize DataFrame to store results for each iteration and role
results = pd.DataFrame()

# Loop over each iteration with tqdm for progress tracking
for iteration in tqdm(range(num_iterations), desc="Overall Progress", unit="iteration"):

    # Set different seed per iteration 
    random_seed = iteration + 100

    # Loop over each role
    for role in roles:
        role_data = grouped_data.get_group(role)

        # Perform Random Forest analysis
        rf_r2, rf_mse, rf_importances = models.perform_random_forest(role_data, seed = random_seed)
        
        # Perform Linear Regression analysis
        lr_r2, lr_mse, lr_coefficients = models.perform_linear_regression(role_data, seed = random_seed)

        # Store results
        iteration_results = pd.concat([rf_importances, lr_coefficients], axis=1)
        iteration_results.columns = [f'{role}_{col}_{iteration}' for col in iteration_results.columns]
        results = pd.concat([results, iteration_results], axis=1)

# Calculate averages of coefficients and importance values across iterations for each role
average_coefficients = pd.DataFrame()
average_importances = pd.DataFrame()

for role in roles:
    role_coefficients = []
    role_importances = []
    for iteration in range(num_iterations):
        rf_col = f'{role}_Importance_{iteration}'
        lr_col = f'{role}_Coefficient_{iteration}'
        role_importances.append(results[rf_col])
        role_coefficients.append(results[lr_col])

    # Calculate averages for coefficients and importance values
    avg_coefficients = pd.concat(role_coefficients, axis=1).mean(axis=1)
    avg_importances = pd.concat(role_importances, axis=1).mean(axis=1)

    # Store averages in separate DataFrames
    average_coefficients[f'{role}_Avg_Coefficient'] = avg_coefficients
    average_importances[f'{role}_Avg_Importance'] = avg_importances

# Combine individual iteration results with average coefficients and importances
final_results = pd.concat([results, average_coefficients, average_importances], axis=1)

# Save to CSV
final_results.to_csv('results.csv')


