def jerigonzo(string):
    string.lower
    vocales = "aeiou"
    palabra = ""
    largo = len(string)
    i=0
    while i<largo:
        c = vocales.find(string[i])
        if c == -1:
            palabra+=string[i]
        else:
            palabra= palabra+string[i]+("p"+string[i]) 
        i+=1
    return palabra
    
if __name__ == "__main__":
    string = input()   
    print(jerigonzo(string))