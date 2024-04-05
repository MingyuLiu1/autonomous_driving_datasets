import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

countries = ['RGB Camera', 'LiDAR', 'Stereo Camera', 'Radar', 'Thermal Camera', 'Event Camera', 'Fisheye Camera']
numbers = [189, 93, 29, 19, 12, 10, 6]
alpha = 0.8
colors = cm.twilight(np.linspace(0, 1, 9)) # twilight Pastel1
colors_with_alpha = [(r, g, b, alpha) for r, g, b, _ in colors]

total = sum(numbers)

fig, ax = plt.subplots(figsize=(13, 11))
# wedges, texts, autotexts = ax.pie(numbers, textprops=dict(color="w"), autopct="")
wedges, texts, autotexts = ax.pie(numbers, textprops=dict(color="w"), autopct="", colors=colors_with_alpha, radius=0.9)

# Show number on each slice
for i, (p, num) in enumerate(zip(wedges, numbers)):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    ax.text(x*0.7, y*0.7, str(num), ha="center", va="center", color="black", fontsize='26')

# Add a white edge for each country
for wedge in wedges:
    wedge.set_edgecolor('black')

for i, (country, num, p) in enumerate(zip(countries, numbers, wedges)):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = f"angle,angleA=0,angleB={ang}"
    percent = round(num / total * 100, 2)
    
    if country == 'RGB Camera':
        xytext = (0.5 * np.sign(x), y * 1.1) 
        connectionstyle += ",rad=0.0" 
        xy=(x*0.9, y*0.9)
    elif country == 'LiDAR':
        xytext = (0.7 * np.sign(x), y * 1.1) 
        connectionstyle += ",rad=0.0" 
        xy=(x*0.9, y*0.9)
    elif country == 'Stereo Camera':
        xytext = (0.9 * np.sign(x), y*1.2) 
        connectionstyle += ",rad=0.5" 
        xy=(x*0.9, y*0.9)
    elif country == 'Radar':
        xytext = (1.4 * np.sign(x), y * 1.3) 
        connectionstyle += ",rad=0.5" 
        xy=(x*0.9, y*0.9)
    elif country == 'Thermal Camera':
        xytext = (1.1 * np.sign(x), y*1.5)  
        connectionstyle += ",rad=0.5"
        xy=(x*1.1-0.2, y)
    elif country == 'Fisheye Camera':
        xytext = (1.1 * np.sign(x), y*1.7)
        connectionstyle += ",rad=0.5" 
        xy=(x*0.9, y*0.9)
    elif country == 'Event Camera':
        xytext = (1.1 * np.sign(x), y-0.1) 
        connectionstyle += ",rad=0.0" 
        horizontalalignment='left'
        xy = (x*0.9, y)
    else:
        xytext = (1.1 * np.sign(x), y * 1.5)
        connectionstyle += ",rad=0.5"

    ax.annotate(f"{country} {percent}%", xy=xy, xytext=xytext,
                horizontalalignment=horizontalalignment, verticalalignment='center', fontsize='35',
                arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle))


plt.subplots_adjust(top=0.98, bottom=0.02, left=0.02, right=0.98)
plt.show()

plt.savefig("sensor_dist.pdf", dpi=200, bbox_inches='tight')
