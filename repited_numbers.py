# having and array, find which is a repited number.

def main(data):

    data.sort()
    
    for i in range(len(data)):
        if data[i] == data[i+1]:
            return data[i]
        
print(main([1, 4, 3, 2, 6, 3]))