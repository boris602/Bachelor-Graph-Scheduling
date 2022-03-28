import matplotlib.pyplot as plt
import numpy as np


labels = ['1', '(1,2)', '[2,3)', '[3,4)', '4','5', '6']
bars1 = [362781, 368631, 243422,22822, 2038, 298, 8]
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
#ax.set_title(r"Testreihe 3 für $K_6$",  fontweight='bold',size=13)
plt.yscale('log')
ax.set_ylim(ymin=1)
ax.set_ylim(ymax=1000000)
ax.text(0.95, 0.9, 'max = 6',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='darkgreen', fontsize=12)
ax.text(0.96, 0.8, r' avg $\approx 1.49$',
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='orange', fontsize=12)

for rect, label in zip(rects1, bars2):
    height = rect.get_height()
    ax.text(
        rect.get_x() + rect.get_width() / 2,
        height + 5, label, ha="center", va="bottom"
    )

plt.show()

fig.tight_layout()

plt.show()