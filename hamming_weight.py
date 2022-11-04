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
