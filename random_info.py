# whith this program you will shuffle a list of elements of the lenght that you want.

import random

def main():

    list = []

    n = int(input("How many elements do you want? "))
    x = 0

    while x <= (n-1):
        i = input("Element: ")
        list.append(i)
        x += 1

    random.shuffle(list)

    for y in list:
        print(y)
    main()

main()

