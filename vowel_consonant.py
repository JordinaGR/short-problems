# program to check if the character is a vowel or consonant
data = str(input('Write here: '))

vowelArr = ['a', 'e', 'i', 'o', 'u']
consonantVar = "bcdfghjklmnpqrstvwxyz"
spaceArr = [' ']
consonantArr = []

result = []

for i in consonantVar:
	consonantArr.append(i)

def check(data):
	i = 0
	leng = int(len(data))

	while leng > i:
		for j in vowelArr:
			if data[i] == j:
				result.append('V')

		for x in consonantArr:
			if data[i] == x:
				result.append('C')

		for y in spaceArr:
			if data[i] == y:
				result.append('  ')

		i += 1

check(data)
for h in result:
	print(h, end="")