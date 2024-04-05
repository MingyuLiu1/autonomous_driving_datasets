import json 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
import math

"""
# Load in all the different dataset data

#Argovers2
argoverse2_OPF = []
with open("Argoverse2_Obj_per_frame.json", "r") as f:
    argoverse2_data= json.load(f)
    argoverse2_OPF = list(argoverse2_data.values())

print("Argoverse 2 load complete")

#KITTI
kitti_OPF = []
with open("KITTI_Obj_per_frame.json", "r") as f:
    kitti_OPF = json.load(f)
print("KITTI load complete")

#nuScenes
nuscenes_OPF = []
with open("nuScenes_Obj_per_frame_2.json", "r") as f:
    nuscenes_OPF = json.load(f)
print("nuScenes load complete")

#ONCE
once_OPF = []
with open("ONCE_Obj_per_frame.json", "r") as f:
    once_OPF = json.load(f)
print("ONCE load complete")

#Waymo
waymo_OPF = []
with open("Waymo_Obj_per_frame.json", "r") as f:
    waymo_OPF = json.load(f)
print("Waymo load complete")

#ZOD
zod_OPF = []
with open("ZOD_Obj_per_frames.json", "r") as f:
    zod_OPF = json.load(f)
print("ZOD load complete")

"""



# List of data file names
data_files = ["Argoverse2_Obj_per_frame.json", 'KITTI_Obj_per_frame.json', 'nuScenes_Obj_per_frame_2.json', 'ONCE_Obj_per_frame.json', 'Waymo_Obj_per_frame.json', 'ZOD_Obj_per_frames.json']

color_palette = ["blue", "red", "green", "orange", "purple", "lightblue"]

label_names=["Argoverse2", "KITTI", "nuScenes", "ONCE", "Waymo", "ZOD"]


# Initialize the figure
plt.figure(figsize=(12, 8))
ax = plt.gca()

index = 0
# Loop through each data file
for data_file in data_files:
    # Load data from the JSON file
    if data_file == "Argoverse2_Obj_per_frame.json":
        with open(data_file, 'r') as f:
            data = json.load(f)
        numbers = list(data.values())
    else:
        with open(data_file, 'r') as f:
            numbers = json.load(f)
    
    

    # Convert the values to floats
    numbers = [float(x) for x in numbers]

    # Create a histogram to get the count of frames for each number of objects
    hist, bins = np.histogram(numbers, bins=np.arange(min(numbers), max(numbers) + 1.5))
    
    # # Smooth the histogram line using a moving average
    # window = 3  # Adjust the window size as needed
    # smoothed_hist = np.convolve(hist, np.ones(window)/window, mode='same')
    
    # Plot the smoothed histogram line
    plt.plot(bins[:-1], hist, label=label_names[index], color=color_palette[index])  # Remove '.json' from label

    # Fill the area under the line
    plt.fill_between(bins[:-1], hist, alpha=0.3, color=color_palette[index])

    index+=1

# Set plot labels and title
plt.xlabel('Number of Objects per Frame', fontsize='24')
plt.ylabel('Count of Frames', fontsize='24')


# Set x and y axis limits to start at 0
plt.xlim(0,250)
plt.ylim(0)

# Show a legend
plt.legend(fontsize="24")
plt.rcParams.update({"font.size":40})
# plt.tick_params(axis='x', labelsize='x-large')
# plt.tick_params(axis='y', labelsize='x-large')
# Adjust the spacing around the plot
# plt.subplots_adjust(left=0.08, right=0.95, bottom=0.08, top=0.95)

plt.tick_params(axis="x", labelsize='20')
plt.tick_params(axis="y", labelsize='20')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.subplots_adjust(left=0.1, right=0.96, top=0.95, bottom=0.1)
# Display the plot
plt.show()
plt.savefig("Obj_per_frame.png", dpi=500)


















