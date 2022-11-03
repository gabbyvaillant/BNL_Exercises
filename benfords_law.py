#!/usr/bin/env python3
# benfords_law.py
import matplotlib.pyplot as plt
import os
import sys
import random


def create_list():
    random_list = random.sample(range(1, 1_000_000), 100_000) # generate desired list of numbers
    return [i ** 100 for i in random_list] # raise to the 100th power


def count(list):
    counting = [] # initialize a empty list
    for i in list:
        aux = str(i)  # placeholder variable to modify each element i into a string
        counting.append(int(aux[0])) # add the first digit of each element to our counting list
    return counting


# Creating Histogram:
def plot(ax):
    a = count(create_list())  # the list of the first digits
    b = [1,2,3,4,5,6,7,8,9,10] # different possibilities of digits
    ax.hist(a, bins = b, color = "maroon", density = "True") # need to fix the bar graph
    ax.set_title(f"Benford's Law")
    plt.ylabel('Probability')
    plt.xlabel('Leading Digit')


def main():
    fig = plt.figure(os.path.basename(sys.argv[0]))
    gs = fig.add_gridspec(1, 1)

    ax = fig.add_subplot(gs[0, 0])
    plot(ax)

    plt.show()

if __name__ == "__main__":
    main()
