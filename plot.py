import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

data = pd.read_csv(
    'data.csv',
    header=None,
    index_col=0,
).squeeze("columns").to_dict()

""" Data from https://hexaco.org/hexaco-inventory. """
hexaco = {
    'h': {
        'domain': 'Honesty',
        'mean': 3.19,
        'stdev': 0.62,
        'color': 'orange',
    },
    'e': {
        'domain': 'Emotionality',
        'mean': 3.43,
        'stdev': 0.62,
        'color': 'green',
    },
    'x': {
        'domain': 'Extraversion',
        'mean': 3.50,
        'stdev': 0.57,
        'color': 'blue',
    },
    'a': {
        'domain': 'Agreeableness',
        'mean': 2.94,
        'stdev': 0.58,
        'color': 'red',
    },
    'c': {
        'domain': 'Conscientiousness',
        'mean': 3.44,
        'stdev': 0.56,
        'color': 'grey',
    },
    'o': {
        'domain': 'Openness',
        'mean': 3.41,
        'stdev': 0.60,
        'color': 'violet',
    },
}

fig, ax = plt.subplots(2, 3)
score_range = np.arange(1, 5, 0.01)

i = 0
j = 0

for key in hexaco:

    mean = hexaco[key]['mean']
    stdev = hexaco[key]['stdev']
    color = hexaco[key]['color']
    domain = hexaco[key]['domain']
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
