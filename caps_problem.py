data = ['F', 'B','B', 'F', 'B', 'F','B', 'F']

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        data[i+1] = data[i]

print(data)