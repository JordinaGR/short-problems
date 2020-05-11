data = "get_repited_characters"
arr = []

for j in data:
	arr.append(j)

print('String to be analized: ')
for i in arr:
	print(i, end='')
print('\n')

arr.sort()

print('Sorted string: ')
for i in arr:
	print(i, end=' ')
print('\n')

print('Repited characters: ')
def main(arr):
	if len(arr) <= 1 or len(arr) <= 0:
		quit()
	elif arr[0] != arr[1]:
		del arr[0]
		return main(arr)

	elif arr[0] == arr[1]:
		print(arr[0], end=', ')
		del arr[0]
		del arr[0]
		return main(arr)

main(arr)
