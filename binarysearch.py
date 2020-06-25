#A simple binary search, data is the array, val is the number you are looking for.

def binary_search(data, val):
    if len(data)==0 or (len(data)==1 and data[0]!=val): #When there are no values or one that that's not our value
        print("false")  #the value is not here and quit
        quit()

    mid = data[len(data)//2]    #here i get the midpoin of the array

    if mid == val:
        print("True")   #value found
        quit()
    if mid > val: return binary_search(data[:len(data)//2], val)  # It returns half of the array (where val is)
    if mid < val: return binary_search(data[len(data)//2+1:], val)

a = [1,2,4,5,6,7,8,9]   #Any sorted array
binary_search(a, 5) #Call the function