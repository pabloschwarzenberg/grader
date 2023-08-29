def jerigonzo(string):
    palabra = list(string)
    
    for i in range(len(palabra)):
        x = palabra[i]
        if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
            palabra[i] = x+"p"+x
            
    string = "".join(map(str, palabra))
    
    return string

if __name__ == "__main__":
    pass
         