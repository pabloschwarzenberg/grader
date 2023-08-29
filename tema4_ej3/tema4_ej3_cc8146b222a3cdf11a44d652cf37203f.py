def jerigonzo(palabra):

    palabra_nueva = ""
    for i in palabra:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            palabra_nueva = palabra_nueva + i + "p" + i
       
        else:
            palabra_nueva = palabra_nueva + i
    
    return palabra_nueva

if __name__ == "__main__":

    print(jerigonzo(input("Ingresa una palabra: ")))