import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


# Read the CSV file into a pandas DataFrame
csv_file = 'BT_Domain_Year.csv'  # Replace with the actual file path
csv = pd.read_csv(csv_file, header=None)  # No header in the CSV

# print(csv)

# Create a histogram plot for each attribute over the years
plt.figure(figsize=(12, 8))
ax = plt.gca()

# Get unique attributes
# attributes = csv[2].unique()
attributes = ['Onboard', 'V2X/V2V/V2I', 'Drone', 'Others']
# attributes = ['V2X' if attribute == 'V2X/V2V/V2I' else attribute for attribute in attributes]

# handles_labels = []

# Define colors for the lines
colors = ['green', 'blue', 'orange', 'purple']

# Define markers for each attribute
markers = ['o', 'x', 's', '^']

# manually add the dataset number for 2023 and 2024
manual_counts_2023 = {
    'Onboard': 21, 
    'V2X': 7,      
    'Drone': 2,    
    'Others': 2    
}

manual_counts_2024 = {
    'Onboard': 5, 
    'V2X': 3,     
    'Drone': 0,    
    'Others': 0    
}


# Loop through each unique attribute, color, and marker
for i, (attribute, color, marker) in enumerate(zip(attributes, colors, markers)):
    subset_df = csv[csv[2] == attribute]
    year_counts = subset_df[1].value_counts().sort_index()
    if attribute == 'V2X/V2V/V2I':
        attribute = 'V2X'
    year_counts.loc[2023] = manual_counts_2023[attribute]
    year_counts.loc[2024] = manual_counts_2024[attribute]   
    plt.plot(year_counts.index, year_counts.values, label=attribute, color=color, marker=marker, linestyle='-')
    
    # Draw cumulative counts
    # cumulative_counts = year_counts.cumsum()
    # line, = plt.plot(cumulative_counts.index, cumulative_counts.values, label=attribute, color=color, marker=marker, linestyle='-')
    # handles_labels.append(line)

# Add labels and legend
plt.xlabel('Year', fontsize='24')
plt.ylabel('Publishing Datasts Number', fontsize='24')
plt.title('Number of Datasets Over the Years', fontsize='24')
plt.legend(fontsize='24')
# print(handles_labels)
# plt.legend(handles=handles_labels, fontsize='xx-large')

# Refine figure
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(False)
# ax.xaxis.grid(False)
# ax.yaxis.grid(True)
plt.tick_params(axis='x', labelsize='20')
plt.tick_params(axis='y', labelsize='20')
xticks = list(range(2008, 2025, 1)) + [2024]
xtickslabel = [str(year) for year in range(2008, 2025, 1)] + ['2024.02']
plt.xticks(xticks, xtickslabel, rotation=45)

# Show the plot
plt.tight_layout()
# plt.show()
plt.savefig("sensing_domain.pdf", dpi=300, bbox_inches='tight')




