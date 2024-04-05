import json 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np


# max_argo = max(argoverse2_distances)
# max_kitti = max(kitti_distances)
# max_nuscenes = max(nuScenes_distances)
# max_waymo = max(Waymo_distances)
# max_once = max(ONCE_distances)
# max_zod = max(ZOD_distances)

# print("Max distances:")
# print(max_argo)
# print(max_kitti)
# print(max_nuscenes)
# print(max_waymo)
# print(max_once)
# print(max_zod)

datasets = [
    ("Argoverse2", "Argoverse2_Obj_Distances.json"),
    ("KITTI", "KITTI_Obj_Distances.json"),
    ("nuScenes", "nuScenes_Obj_Distances.json"),
    ("ONCE", "ONCE_Obj_distances.json"),
    ("Waymo", "Waymo_Obj_Distances.json"),
    ("ZOD", "ZOD_Obj_Distances_<250.json")
]

all_distances = []
list_names = []

for dataset_name, file_name in datasets:
    distances = []
    with open(file_name, "r") as f:
        distances = json.load(f)
    print(f"{dataset_name} load complete with {len(distances)} objects")
    all_distances.extend(distances)
    list_names.extend([dataset_name] * len(distances))

# Create a dataframe from the merged list
df = pd.DataFrame({'Distance in meters': all_distances, 'List': list_names})

# Set a custom color palette for the lists
custom_palette = ["blue", "red", "green", "orange", "purple", "lightblue"]
# custom_palette = ["red", "green", "orange"]

# Initialize the figure
plt.figure(figsize=(12, 8))
ax = plt.gca()

# Plot the histogram with a bin size of one meter for each list
ax = sns.histplot(data=df, x='Distance in meters', hue='List', bins=int(max(all_distances) - min(all_distances)) + 1, kde=True, element='step', palette=custom_palette)

# Set x-axis limit to 250 meters
ax.set_xlim(0, 250)

# Manually create the legend with custom labels and colors
legend_handles = [plt.Line2D([0], [0], color=custom_palette[i], lw=2, label=dataset_name) for i, (dataset_name, _) in enumerate(datasets)]
ax.legend(handles=legend_handles, fontsize='24')
plt.xticks(fontsize="20")
plt.yticks(fontsize="20")

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xlabel('Distance in meters', fontsize='24')
plt.ylabel('Number of Objects',  fontsize='24')

plt.subplots_adjust(left=0.13, right=0.96, top=0.95, bottom=0.1)

# plt.show()

plt.savefig("Obj_Distance_distribution.png", dpi=500)

























