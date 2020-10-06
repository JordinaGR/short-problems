# simple program to delete all the repited characters in a list

def main(data):
	data1 = []

	while len(data) > 0:
		if data[0] not in data1:
			data1.append(data[0])
		else:
			del data[0]

	return data1

print(main([1, 4, 3, 6, 5, 3, 8, 9, 9]))