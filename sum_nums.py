data = [2, 4, 1]
data1 = [3,1,6]
sum = 8

def findsum(data, data1, sum):
    for i in data:
        for j in data1:
            x = j+i
            if x == sum:
                print(f'{i} + {j} = {sum}')
                quit()
    else:
        print('no such operation in this array')

findsum(data, data1, sum)