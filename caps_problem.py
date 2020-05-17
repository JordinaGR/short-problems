# This is a solution for this problem: https://youtu.be/14UlXIZzwE4 Instructor: Srini Devadas
# This is the solution going one time through the array.

data = ['F', 'B', 'B', 'F', 'B', 'F', 'B', 'F']

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        data[i+1] = data[i]

print(data)