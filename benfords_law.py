#!/usr/bin/env python3
# benfords_law.py

import matplotlib.pyplot as plt
import os
import sys
import random

random_list = random.sample(range(1, 1_000_000), 100_000) # generate desired list of numbers

def raise_tenth(list):
    return [i ** 100 for i in list] # raise every element to the 100th power

new_list = raise_tenth(random_list) # declare it a new name

counting = [] # initialize a empty list

for i in new_list:
    aux = str(i)  # placeholder variable to modify each element i into a string
    counting.append(int(aux[0])) # add the first digit of each element to our counting list


def prob(list):
    return [n / 100_000 for n in list]


a = counting  # the data is the amount of times each number appears
b = [1,2,3,4,5,6,7,8,9,10]
 

# Creating histogram
def plot(ax):
    ax.hist(a, bins = b, density = True)
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
















# NEXT STEP:
# Want to count the number of occurrences of a digit in each element of our new_list
# Only want to count the most significant digit
# EXAMPLE: for 1, we want to see how many times 1 occurs as the left-most digits in each element
# Do this for each number up to 9 and then graph it 
