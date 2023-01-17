import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from model import stats

filename = input("CSV file: ")
data = pd.read_csv(
    rf'{filename}.csv',
    index_col=0,
).squeeze("rows").to_dict()

fig, ax = plt.subplots(2, 3)
score_range = np.arange(1, 5, 0.01)

i = 0
j = 0

for key in stats:

    mean = stats[key]['mean']
    stdev = stats[key]['stdev']
    color = stats[key]['color']
    domain = stats[key]['domain']
    score = data[key]

    if j > 2:
        i += 1
        j = 0

    ax[i,j].plot(
        score_range, norm.pdf(score_range, mean, stdev),
        color=color,
    )
    ax[i,j].set_title(
        domain,
        rotation=-90, x=1, y=.5,
        ha='left', va='center',
    )
    ax[i,j].annotate(
        'You', xy=(score, norm.pdf(score, loc=mean, scale=stdev)),
        xytext=(score, norm.pdf(score, loc=mean, scale=stdev) + 0.1 ),
        arrowprops=dict(facecolor='black'),
        horizontalalignment='center', verticalalignment='top',
    )

    j += 1


plt.show()
