def binary_search(data, val):
    if len(data)==0 or (len(data)==1 and data[0]!=val):
        print('false, not found', val)
    try:
        mid = data[len(data)//2]
    except:
        print('Error, try again')
        quit()

    if mid == val: print('true', val)
    if mid>val: return binary_search(data[:len(data)//2], val)
    if mid<val: return binary_search(data[len(data)//2+1:], val)

a = [1,2,4,5,6,7,8,9]
binary_search(a, 8)