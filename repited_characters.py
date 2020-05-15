data = "4629584697465209834752304986549782364598732648576483756837465874"
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

print('Repited values: ')


def main(arr):
	if len(arr) <= 1:
		quit()
	elif arr[0] != arr[1]:
		del arr[0]
		return main(arr)

	else:
		while arr[0] == arr[1]:

			del arr[0]
			print(arr[0])
			del arr[0]

		#print(arr[0], end=', ')
		return main(arr)


main(arr)
