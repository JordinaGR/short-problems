# In this problem, you enter a number and you get the sum of each number untill that.
# E.g. Input: 4 --- Output: 10 // Because 1+2+3+4 (until 4 (your input)) = 10

def whatever(n):
	print(n * (n + 1) // 2)

n = int(input('Number '))
whatever(n)
