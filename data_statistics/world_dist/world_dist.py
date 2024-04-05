import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

countries = ['USA', 'Synthetic', 'Germany', 'Europe', 'China', 'Worldwide', 'Canada', 'Korea', 'UK', 'Japan', 
             'Australia', 'Singapore', 'Others']
numbers = [40, 35, 24, 24, 16, 14, 8, 7, 5, 4, 3, 2, 9]
alpha = 0.8
colors = cm.twilight(np.linspace(0, 1, len(numbers))) # twilight Pastel1
colors_with_alpha = [(r, g, b, alpha) for r, g, b, _ in colors]

total = sum(numbers)

fig, ax = plt.subplots(figsize=(13, 11))
# wedges, texts, autotexts = ax.pie(numbers, textprops=dict(color="w"), autopct="")
wedges, texts, autotexts = ax.pie(numbers, textprops=dict(color="w"), autopct="", colors=colors_with_alpha, radius=0.9)


for i, (p, num) in enumerate(zip(wedges, numbers)):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    ax.text(x*0.7, y*0.7, str(num), ha="center", va="center", color="black", fontsize='22')


for wedge in wedges:
    wedge.set_edgecolor('black')


for i, (country, num, p) in enumerate(zip(countries, numbers, wedges)):
    ang = (p.theta2 - p.theta1) / 2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    verticalalignment = "center"
    connectionstyle = f"angle,angleA=0,angleB={ang},rad=0.5"
    percent = int(num / total * 100)
    
    if country == 'Europe(except Germany)':
        country = "Europe\n(except Germany)"
        xytext = (0.9 * np.sign(x), y * 0.9 if y >= 0 else y * 0.9)
        verticalalignment = 'center'
    else:
        xytext = (1.1 * np.sign(x), y * 1.1)
        
    percent = round(num / total * 100, 2)
    
    ax.annotate(f"{country} {percent}%", xy=(x*0.9, y*0.9), xytext=xytext,
                 horizontalalignment=horizontalalignment, verticalalignment=verticalalignment, fontsize='25',
                 arrowprops=dict(arrowstyle="-", connectionstyle=connectionstyle))

plt.subplots_adjust(top=0.9, bottom=0.1, left=0.05, right=0.95)
plt.show()

plt.savefig("world_dist.pdf", dpi=200, bbox_inches='tight')
