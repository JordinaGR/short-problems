#find all the possible operations to get value "sum" combinating two arrays.

data = [3, 4, 4, 0]
data1 = [3, 2, 6, 5, 3]
sum = 6

def findsum(data, data1, sum):
    for i in data:
        for j in data1:
            x = j+i
            if x == sum:
                print(f'{i} + {j} = {sum}')


findsum(data, data1, sum)