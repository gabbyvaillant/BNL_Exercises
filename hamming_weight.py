# hamming_weight.py

# the hamming weight of an integer
# is amount of digits in that integer which are NOT zero

# write a program that given a number n, the for loop runs through an integer
# and counts the number of digits that are not 1 and then adds one to the total
# sum of numbers which are not zero. That sum is the hamming weight of a number


def hamming(n):
    binary_n = bin(n)[2:]  # bin() prints 0b so we want to get rid of that
    i = 0
    for digit in iter(str(binary_n)):
        if digit != "0":
            i += 1
    return i



print(hamming(95601))
print(bin(95601)[2:])

# Notes:
# Iterate through digits in a number
# need to make 0 a str by putting quotes around it



# dave's way

#!/usr/bin/env python3
# hamming_weight_instructor.py

# See https://en.wikipedia.org/wiki/Hamming_weight


def pop_count(n):
    count_onebits = 0
    while n > 0:
        count_onebits += n % 2 # what the remainder mod 2
        n //= 2  # divide by two each time same as n = n // 2
    return count_onebits


def main():
    n = 95601

    hw = pop_count(n)

    print(f"The Hamming weight of = {n:,}" f" in base 2 is {hw:,}")

    hw = bin(n).count("1")  # count the number of times "1" appears in str. iter through str
    print(f"The Hamming weight of = {n:,}" f" in base 2 is {hw:,}")


if __name__ == "__main__":
    main()
