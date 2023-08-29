def jerigonzo(string):
    return string
    
#jeringonza
#agregar p despues de cada vocal
#repetir la vocal

palabra = input("Ingresa una palabra: ")
translado = ""

for letra in palabra:
    if letra in "AEIOUaeiou":
        translado += letra
        # agregar p despues de la vocal
        translado += "p"
    # repetir la vocal
    translado += letra
    
print(translado)             