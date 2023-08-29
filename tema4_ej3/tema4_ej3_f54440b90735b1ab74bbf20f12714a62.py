def jerigonzo(string):
    suma = ""
    for a in string:
        l_palabra.append(a)

    for n in l_palabra:
        if n in vocales:
          suma += n + "p" + n
        else:
          suma += n
          
    return suma

vocales = ["a", "e", "i", "o", "u"] 
l_palabra = []

if __name__ == "__main__":
    string = input("Ingrese la palabra que sera traducida a jeringonzo: ")

    print(jerigonzo(string))
    pass  
         