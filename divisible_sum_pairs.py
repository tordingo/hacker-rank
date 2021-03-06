#!/bin/python3

import os

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    acc = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                acc += 1

    return acc

if __name__ == '__main__':
    n, k = map(int, input().split())

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
    with open(os.environ['OUTPUT_PATH'], 'w') as fptr:
        fptr.write(str(result) + '\n')
