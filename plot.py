"""Plot HEXACO personality test on normal distribution."""
import argparse
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from model import stats
from scipy.stats import norm

def domain_plot(ax, score_range, score, domain):
    """TODO: Docstring for domain_plot.

    :arg1: TODO
    :returns: TODO

    """

    mean = domain['mean']
    stdev = domain['stdev']
    color = domain['color']
    name = domain['name']

    ax.plot(
        score_range, norm.pdf(score_range, mean, stdev),
        color=color,
    )
    ax.set_title(
        name,
        rotation=-90, x=1, y=.5,
        ha='left', va='center',
    )
    ax.annotate(
        'You', xy=(score, norm.pdf(score, mean, stdev)),
        xytext=(score, norm.pdf(score, mean, stdev) + 0.1 ),
        arrowprops=dict(facecolor='black'),
        horizontalalignment='center', verticalalignment='top',
    )


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    parser = argparse.ArgumentParser(
        prog = 'python3 plot.py',
        description = "Plot HEXACO personality test results on normal distribution.",
    )
    parser.add_argument('results_file', help='file to which output results')
    args = parser.parse_args()
    results_file = args.results_file

    data = pd.read_csv(
        results_file,
        index_col=0,
    ).squeeze("rows").to_dict()

    _, ax = plt.subplots(2, 3)
    score_range = np.arange(1, 5, 0.01)

    i = 0
    j = 0
    for key, domain in stats.items():
        score = data[key]

        if j > 2:
            i += 1
            j = 0

        domain_plot(ax[i,j], score_range, score, domain)

        j += 1

    plt.show()

if __name__ == "__main__":
    main()
