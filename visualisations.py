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
# Co-efficient plot
#----------------------------------------------------------------------------------------------------- # 
# Columns to use for plotting
coefficient_columns = ['Support_Avg_Coefficient', 'ADC_Avg_Coefficient', 'Middle_Avg_Coefficient',
                       'Jungle_Avg_Coefficient', 'Top_Avg_Coefficient']

# Colors for each column
colors = ['blue', 'orange', 'green', 'red', 'purple']

# Generate y-values as an array of equally spaced integers
y_values = np.arange(len(visualisation_results))

# Plotting
plt.figure(figsize=(10, 8))

for i, column in enumerate(coefficient_columns):
    x_values = visualisation_results[column]
    plt.scatter(x_values, y_values, color=colors[i], label=column, alpha=0.6)

# Plot customization
plt.xlabel('Coefficient Values')
plt.ylabel('Y Labels')
plt.yticks(y_values, visualisation_results.index)  
plt.title('Average Coefficients Comparison')
plt.legend()
plt.tight_layout()

plt.show()


#----------------------------------------------------------------------------------------------------- #
# Importance plot
#----------------------------------------------------------------------------------------------------- # 
# Columns to use for plotting
importance_columns = ['Support_Avg_Importance', 'ADC_Avg_Importance', 'Middle_Avg_Importance',
                      'Jungle_Avg_Importance', 'Top_Avg_Importance']

# Colors for each column
colors = ['blue', 'orange', 'green', 'red', 'purple']

# Generate y-values as an array of equally spaced integers
y_values = np.arange(len(visualisation_results))

# Plotting
plt.figure(figsize=(10, 8))

for i, column in enumerate(importance_columns):
    x_values = visualisation_results[column]
    plt.scatter(x_values, y_values, color=colors[i], label=column, alpha=0.6)

# Plot customization
plt.xlabel('Importance Values')
plt.ylabel('Y Labels')
plt.yticks(y_values, visualisation_results.index)  
plt.title('Average Importance Comparison')
plt.legend()
plt.tight_layout()

plt.show()