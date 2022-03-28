import matplotlib.pyplot as plt
import numpy as np


labels = ['1', '(1,2)', '[2,3)', '3', '4', '5']
bars1 = [5514718, 2365032, 1855754, 242197, 20810, 1489]
bars2 = [str(i) for i in bars1]


x = np.arange(len(labels))
width = 0.35

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

rects = ax.bar(x, bars1, width)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Anzahl', fontweight='bold', size=11)
ax.set_xlabel("Approximationsfaktor", fontweight='bold', size=11)
ax.set_xticks(x, labels)
#ax.set_title(r"Testreihe 3 für $K_5$",  fontweight='bold',size=13)
plt.yscale('log')
ax.set_ylim(ymin=1000)
ax.set_ylim(ymax=10000000)
ax.text(0.95, 0.9, 'max = 5',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='darkgreen', fontsize=12)
ax.text(0.96, 0.8, r' avg $\approx 1.37$',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='orange', fontsize=12)

for rect, label in zip(rects, bars2):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2,
        height + 5, label, ha="center", va="bottom"
    )

plt.show()

fig.tight_layout()

plt.show()