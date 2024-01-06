#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#----------------------------------------------------------------------------------------------------- #
# Load results 
#----------------------------------------------------------------------------------------------------- # 
visualisation_results = pd.read_csv('model_results.csv', index_col = 0)


#----------------------------------------------------------------------------------------------------- #
# Scatter plot function
#----------------------------------------------------------------------------------------------------- # 
def create_scatter_plot(data: pd.DataFrame, columns: list, title: str, xlabel: str):
    """
    Parameters:
        data (DataFrame): The DataFrame containing the data to plot
        columns (list): List of column names to be plotted
        title (str): Title of the plot
        xlabel (str): Label for the X-axis

    """
    # Colors for each column
    colors = ['blue', 'orange', 'green', 'red', 'purple']

    # Generate y-values as an array of equally spaced integers
    y_values = np.arange(len(data))

    # Plotting
    plt.figure(figsize=(10, 8))

    for i, column in enumerate(columns):
        x_values = data[column]
        plt.scatter(x_values, y_values, color = colors[i], label = column, alpha = 0.6)

    # Plot customization
    plt.xlabel(xlabel)
    plt.ylabel('Y Labels')
    plt.yticks(y_values, data.index)  
    plt.title(title)
    plt.legend()
    plt.tight_layout()

    plt.show()


#----------------------------------------------------------------------------------------------------- #
# Data columns
#----------------------------------------------------------------------------------------------------- # 
methods_list = ['Coefficient', 'rf_Importance', 'xg_Importance']

columns_dict = {}

for name in methods_list: 
    columns_dict[name + '_columns'] = ['Support_Avg_' + name, 'ADC_Avg_' + name, 'Middle_Avg_' + name,
                                       'Jungle_Avg_' + name, 'Top_Avg_' + name]
        
Coefficient_columns = columns_dict['Coefficient_columns']
rf_Importance_columns = columns_dict['rf_Importance_columns']
xg_Importance_columns = columns_dict['xg_Importance_columns']


#----------------------------------------------------------------------------------------------------- #
# (Linear Regression) Co-efficient plot
#----------------------------------------------------------------------------------------------------- # 
create_scatter_plot(visualisation_results, Coefficient_columns, 'Average Coefficients Comparison', 'Coefficient Values')


#----------------------------------------------------------------------------------------------------- #
# (Random Forest) Importance plot
#----------------------------------------------------------------------------------------------------- # 
create_scatter_plot(visualisation_results, rf_Importance_columns, 'Average RF Importance Comparison', 'rf_Importance Values')


#----------------------------------------------------------------------------------------------------- #
# (xgboost) Importance plot
#----------------------------------------------------------------------------------------------------- # 
create_scatter_plot(visualisation_results, xg_Importance_columns, 'Average xg Importance Comparison', 'xg_Importance Values')