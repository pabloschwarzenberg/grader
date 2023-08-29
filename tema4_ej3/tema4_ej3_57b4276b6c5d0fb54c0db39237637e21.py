def jerigonzo(string):
    vocales = ['a', 'e', 'i', 'o', 'u']
    temp = list(string)
    i = 0
    while i < len(temp):
        if temp[i] in vocales:
            temp.insert(i+1, temp[i])
            temp.insert(i+1, 'p')      
            i += 2    
        i += 1
    string = ''.join(temp)
    return string

if __name__ == "__main__":
    pass
         