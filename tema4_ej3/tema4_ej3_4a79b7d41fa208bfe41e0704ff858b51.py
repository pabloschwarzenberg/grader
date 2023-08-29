if __name__ == "__main__": 
    string = input("Ingrese un string: ")
    jerigonzo(string)
    
def jerigonzo(string):
    string_traducido = ""
    vocales = ["a", "e", "i", "o", "u"]
    for i in range(len(string)):
        caracter = string[i]
        if caracter=="a" or caracter== "e" or caracter== "i" or caracter=="o" or caracter=="u":
            string_traducido += caracter+"p"+caracter
        else:
            string_traducido+=caracter
    
    return string_traducido
            