import os
import json
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.colors import LogNorm # matplotlib >= 3.4.0


path = "./dataset_survey/data_statistics/All_Datasets_Data/360_Distribution/"

names = ["Argoverse2", "KITTI", "Waymo", "nuScenes", "ONCE", "ZOD"]
coords_list = []
if_argo = True

# figure out max value
global_max = None
for name in names: 
    filepath = path+name+"_xy_coord.json"
    with open(filepath, "r") as f:
        xy_coords = json.load(f)
    # if if_argo ==  True:
    #     x_values = [coord[1] for coord in xy_coords]
    #     y_values = [coord[0] for coord in xy_coords]
    #     if_argo = False
    # else:
    x_values = [coord[0] for coord in xy_coords]
    y_values = [coord[1] for coord in xy_coords]
    hist, _, _ = np.histogram2d(x_values, y_values, bins=100)
    local_max = np.max(hist)
    local_max = 250000
    global_max = local_max if global_max is None else max(global_max, local_max)
    coords_list.append(xy_coords)

# Create a 2x3 grid of subplots
fig, axes = plt.subplots(2, 3, figsize=(22, 12))
if_argo = True
# Loop through the coordinates lists and create plots in the grid
for i, (coords, ax) in enumerate(zip(coords_list, axes.flatten())):
    if if_argo ==  True:
        x_values = [coord[1] for coord in coords]
        y_values = [coord[0] for coord in coords]
        if_argo = False
    else:
        x_values = [coord[0] for coord in coords]
        y_values = [coord[1] for coord in coords]
        
    x_bins = np.linspace(-100, 100, 100)
    y_bins = np.linspace(-100, 100, 100)

    hist = ax.hist2d(x_values, y_values, bins=[x_bins, y_bins], cmap='viridis', norm=LogNorm(vmin=1, vmax=global_max))

    ax.set_title(names[i], fontsize='40', fontname="Times New Roman Bold")
    # if i >=3:
    #     ax.set_xlabel('X Coordinates', fontsize=25)
    # if i % 3 == 0:
    #     ax.set_ylabel('Y Coordinates', fontsize=25)
    # ax.set_xlabel('X Coordinates', fontsize='25')
    # ax.set_ylabel('Y Coordinates', fontsize='25')
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)
    ax.set_aspect('equal', adjustable='box')
    ax.tick_params(axis='x', labelsize='30')
    ax.tick_params(axis='y', labelsize='30')
    ax.set_xticks([-100, -50, 0, 50, 100]) # fontsize=40
    ax.set_yticks([-100, -50, 0, 50, 100])
    
fig.supxlabel('Y Coordinates', fontsize=40, ha='center', fontname="Times New Roman Bold") 
fig.supylabel('X Coordinates', fontsize=40, va='center', fontname="Times New Roman Bold") 

# Use the hist values of the first subplot to create a common colorbar
cbar_ax = fig.add_axes([0.9, 0.1, 0.02, 0.8])  # Adjust the position and size of the colorbar
# cbar = fig.colorbar(hist[3], cax=cbar_ax, label='Number of objects (log)')
cbar = fig.colorbar(hist[3], cax=cbar_ax)
cbar.set_label("Number of obejcts (log)", size=40)
cbar.ax.tick_params(axis='both', labelsize=40)
# Adjust layout and show plots
plt.tight_layout(rect=[0, 0, 0.9, 1])  # Adjust the rectangle in which to constrain the tight_layout
plt.savefig("bev_dist.png", dpi=500)
