#!/usr/bin/python3

import sys

def factorize_number(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i
    return None

def factorize_file(file_path):
    with open(file_path, 'r') as file:
        for line in file_path:
            number = int(line)
            factors = factorize_number(number)
            if factors:
                print(f"{number}={factors[0]}*{factors[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    file_path = sys.argv[1]
    factorize_file(file_path)
