palabra = input("Ingrese una palabra: ")
translado = ""

for letra in palabra:
    if letra in "AEIOUaeiou":
       translado += letra
       
       translado += "P"
       
    translado += letra

print(translado)
    

         