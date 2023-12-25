#----------------------------------------------------------------------------------------------------- # 
# Modules
#----------------------------------------------------------------------------------------------------- # 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#----------------------------------------------------------------------------------------------------- #
# Load results 
#----------------------------------------------------------------------------------------------------- # 
visualisation_results = pd.read_csv('results.csv', index_col = 0)
print(visualisation_results)


#----------------------------------------------------------------------------------------------------- #
# Plot results
#----------------------------------------------------------------------------------------------------- # 
# Columns to use for plotting
columns_to_plot = ['Support_Avg_Coefficient', 'ADC_Avg_Coefficient', 'Middle_Avg_Coefficient',
                   'Jungle_Avg_Coefficient', 'Top_Avg_Coefficient']

# Colors for each column
colors = ['blue', 'orange', 'green', 'red', 'purple']

# Generate y-values as an array of equally spaced integers
y_values = np.arange(len(visualisation_results))

# Plotting
plt.figure(figsize=(10, 8))

for i, column in enumerate(columns_to_plot):
    x_values = visualisation_results[column]
    jitter = np.random.normal(0, 0.1, size=len(y_values))  # Adding a jitter for better visualization
    plt.scatter(x_values + jitter, y_values, color=colors[i], label=column, alpha=0.6)

# Plot customization
plt.xlabel('Coefficient Values')
plt.ylabel('Y Labels')
plt.yticks(y_values, visualisation_results.index)  # Set y-tick labels as index values
plt.title('Average Coefficients Comparison')
plt.legend()
plt.tight_layout()

plt.show()