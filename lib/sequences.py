#!/usr/bin/env python3

def print_fibonacci(length):
    count = 0
    fib_sequence = [0, 1]
    num1 = fib_sequence[-2]
    num2 = fib_sequence[-1]

    if length <= 0:
        print([])

    elif length == 1:
        print([0])

    elif length == 2:
        print([0, 1])

    else:
        while count <= (length - 3):
            num3 = num1 + num2
            fib_sequence.append(num3)
            num1 = num2
            num2 = num3
            count += 1
        print(fib_sequence)

print_fibonacci(12)