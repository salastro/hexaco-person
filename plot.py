"""Plot HEXACO personality test on normal distribution."""
from model import stats
from scipy.stats import norm
from sys import argv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filename = argv[1]
data = pd.read_csv(
    filename,
    index_col=0,
).squeeze("rows").to_dict()

fig, ax = plt.subplots(2, 3)
score_range = np.arange(1, 5, 0.01)

i = 0
j = 0

for key, value in stats.items():

    mean = value['mean']
    stdev = value['stdev']
    color = value['color']
    domain = value['domain']
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
        'You', xy=(score, norm.pdf(score, mean, stdev)),
        xytext=(score, norm.pdf(score, mean, stdev) + 0.1 ),
        arrowprops=dict(facecolor='black'),
        horizontalalignment='center', verticalalignment='top',
    )

    j += 1


plt.show()
