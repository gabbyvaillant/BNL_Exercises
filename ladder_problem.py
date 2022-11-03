#!/usr/bin/env python3
# ladder_problem.py

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import os
import sys

# TASK: Create a Python program called ladder_problem.py that uses SciPy to calculate
#  and display the maximum ladder length possible that will fit around the corner.
#  Additionally, using pyplot, graph the function describing the maximal ladder length as a function of 𝜃
# Finally, plot the point where this function has a zero rate of change.
# The dimensions of the hallways are c1 = 1 and c2 = 2.

def f(x):
    return (1 / np.cos(x)) + (2 / np.sin(x))


def plot(ax):
    a = 0
    b = np.pi / 2

    x = np.linspace(a, b, 1000)
    y = f(x)

    minimum = optimize.minimize(f, x0=0.01)
    y_min = minimum.fun
    x_min = minimum.x

    ax.set_title(f"Maximum Ladder Length")
    ax.set_xlabel(rf"$\theta$")
    ax.set_ylabel("Ladder length")
    ax.grid()
    ax.set_ylim(0, 20)
    ax.axhline(y=0.0, color="lightgray")
    ax.plot(x, y, color="blue", label=rf"Maximal ladder length as a fn of $\theta$")
    plt.plot(x_min, y_min, marker="o", markersize=8, markeredgecolor="red", markerfacecolor="green", label="Minimum",)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.legend(loc="upper right")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()
    print()


if __name__ == "__main__":
    main()
