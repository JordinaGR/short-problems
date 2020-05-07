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
