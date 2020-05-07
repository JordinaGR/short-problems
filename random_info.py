import random

def main():

    llista = []

    n = int(input("Quants elements vols ficar? "))
    x = 0

    while x <= (n-1):
        i = input("Element: ")
        llista.append(i)
        x += 1

    random.shuffle(llista)

    for y in llista:
        print(y)
    main()

main()

