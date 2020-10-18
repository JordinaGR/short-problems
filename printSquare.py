# Print a square, w is the number of rows and columns. This one will be a 6x6 square

w = 6
n = 0

while n < w:
	print('\n')
	for _ in range(w):
		print('*', end='   ')

	n += 1