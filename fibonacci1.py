# You input a position and the output will be that position number.
# E.g input: 4, output: 3 // sequence: 1,1,2,3,5,8...  In the position four there's the number 3.

n = int(input('num '))
a, b = 0, 1
i = 0
list = []

while True:
    if i < n:
        list.append(b)
    else:
        break

    a, b, = b, a+b
    i += 1

print(list[-1])
