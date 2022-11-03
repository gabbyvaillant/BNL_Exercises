#!/usr/bin/env python3
# eulers_constant.py

import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import os
import sys
import scipy.integrate


def harmonic_nums(n):
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
    return h


def f(x):
    return np.log(np.log(1 / x))


def plot(ax):
    a = 0
    b = 50
    Y = -scipy.integrate.quad(f, 0, 1)[0]

    x = np.linspace(a, b)
    y = Y + np.log(x)

    hy = [harmonic_nums(j) for j in range(1, 51)]  # create a list of the harmonic numbers

    ax.set_title(rf"$Y + ln(x)$")
    ax.set_xlabel(rf"$x$")
    ax.set_ylabel(rf"$y$")
    ax.grid()
    ax.set_ylim(0, 6)
    ax.axhline(y=0.0, color="lightgray")
    ax.plot(x, y, color="blue", label=rf"$Y + ln(x)$")
    ax.step(x, y, color="red", label="Harmonic Numbers")

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