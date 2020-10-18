# program to check if the character is a vowel or a consonant

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

'''---------------------------same program commented below--------------------------------------------

data = str(input('Write here: ')) # this is the string you want to know if these are vowels or 
								  # consonants. You can enter letters, words and sentences separated
								  # by spaces. Don't use special characters or you will get an error.
								  # Just letters and spaces.

vowelArr = ['a', 'e', 'i', 'o', 'u'] 	# list with the vowels
consonantVar = "bcdfghjklmnpqrstvwxyz"	# string with the consonants
spaceArr = [' ']	# space character
consonantArr = []	# emty list to put the consonants

result = []	# list where we will append the results (e.g: "hello world" would be: CVCCV CVCCC)

for i in consonantVar: # create the content of the consonant list
	consonantArr.append(i)

def check(data): # main function

	i = 0	# value used in the while loop, as index for the string you entered in var data
	leng = int(len(data)) # length of the data variable 

	while leng > i: # we will iterate each letter and check if it's a vowel, consonant 
					# or space, then add the result in the result list and print it out.
					# the loop will end when the i variable is bigger or equal than the 
					# data length.

		for j in vowelArr:	# check if the letter is in the vowel list if it is append V to the result
			if data[i] == j:
				result.append('V')

		for x in consonantArr: # check if the letter is in the consonant list if it is append C to the result
			if data[i] == x:
				result.append('C')

		for y in spaceArr: 	# check if is a space if it is add two spaces to the result list 
			if data[i] == y: 
				result.append('  ')

		i += 1	# change i value, so you will do the same with the next character

check(data)	# call the function
for h in result:	# print the list result in a pretty way.
	print(h, end="")

'''