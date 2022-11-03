#!/usr/bin/env python3
# archimedes_spiral.py

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

# TASK: Create a Python program called archimedes_spiral.py that uses SciPy to calculate and display 
# the arc length of an Archimedes Spiral with 𝑟=𝜃 as it rotates from 0≤𝜃≤8𝜋.
# Using pyplot, graph this entire spiral.


def f(theta):
    return np.sqrt((theta**2) + 1)


def main():
    theta = np.linspace(0, 8 * np.pi, 1_000)

    arc_length = scipy.integrate.quad(f, 0, 8 * np.pi)[0]
    print(f"The arc length is {arc_length:.2f}")

    a = 0
    b = 1

    plt.polar(theta, a + b * theta)
    plt.plot

    plt.show()


if __name__ == "__main__":
    main()
