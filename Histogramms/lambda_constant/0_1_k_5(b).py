import matplotlib.pyplot as plt
import numpy as np


labels = ['1', '1.5', '2', '3', '4']
bars1 = [3987811, 1546450, 3886829, 557337, 21573]
bars2 = [str(i) for i in bars1]
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)

rects = ax.bar(x, bars1, width)

ax.set_ylabel('Anzahl', fontweight='bold',size=11)
ax.set_xlabel("Approximationsfaktor", fontweight='bold', size=11)
ax.set_xticks(x, labels)
#ax.set_title(r"Testreihe 1 für $K_5$",  fontweight='bold',size=13)
ax.set_ylim(ymin=10000)
ax.set_ylim(ymax=10000000)
plt.yscale('log')
ax.text(0.95, 0.9, 'max = 4',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='darkgreen', fontsize=12)
ax.text(0.96, 0.8, r' avg $\approx 1.59$',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='darkorange', fontsize=12)

for rect, label in zip(rects, bars2):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2,
        height + 5, label, ha="center", va="bottom"
    )

plt.show()

fig.tight_layout()

plt.show()