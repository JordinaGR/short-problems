# recursive program to calculate factorials. Only positive numbers.

def fractorial(n):
	if n >= 1: 
		return n * fractorial(n - 1)
	else:
		return 1
print(fractorial(0))
