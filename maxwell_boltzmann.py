#!/usr/bin/env python3
# maxwell_boltzmann.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
import os
import sys


# Write the PDF:
# I did this in parts because it was easier for me to make sure I inputted it correctly
def my_dist(x, a):
    part_1 = np.sqrt(2 / np.pi)
    part_2 = (x**2) * (np.exp((-(x**2)) / (2 * (a**2))))
    part_3 = (part_2) / (a**3)
    return part_1 * part_3

# Plot the function:
def plot(ax):
    a = 0
    b = 20
    a_1 = 1
    a_2 = 2
    a_3 = 5

    x = np.linspace(a, b)
    y_1 = my_dist(x, a_1)
    y_2 = my_dist(x, a_2)
    y_3 = my_dist(x, a_3)

    ax.set_title(f"Maxwell-Boltzmann Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("P(x)")
    ax.grid()
    ax.set_ylim(0, 0.6)
    ax.axhline(y=0.0, color="lightgray")
    ax.plot(x, y_1, color="blue", label=rf"a = 1")
    ax.plot(x, y_2, color="red", label=rf"a = 2")
    ax.plot(x, y_3, color="green", label=rf"a = 5")

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.legend(loc="upper right")


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()


if __name__ == "__main__":
    main()
