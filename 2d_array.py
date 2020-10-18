#problem from HakerRank: https://www.hackerrank.com/challenges/2d-array/problem

import random

# main function
def hourglassSum(arr):
    sums = []

    for i in range(1, 5):
        for j in range(1, 5):

            sum_values = arr[i][j] + arr[i-1][j-1] + arr[i-1][j+1] + arr[i-1][j] + arr[i+1][j] + arr[i+1][j-1] + arr[i+1][j+1]
            sums.append(sum_values)

    return max(sums)

#create random array
arr = [[random.randint(0, 99) for i in range(0, 6)] for j in range(0, 6)]

#dysplay the array
for i in range(len(arr)):
    print(' ')
    for j in range(len(arr)):
        print("%02d" % arr[i][j], end='| ')

print('\n\n', hourglassSum(arr))

