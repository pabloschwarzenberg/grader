def rot13(palabra):
    lista_1="abcdefghijklm"
    lista_2="nopqrstuvwxyz"
    palabra_encriptada=""
    for letra in palabra:
        if  letra in lista_1:
            ubicacion=lista_1.find(letra)
            palabra_encriptada+=lista_2[ubicacion]
        elif    letra in lista_2:
            ubicacion=lista_2.find(letra)
            palabra_encriptada+=lista_1[ubicacion]
    return palabra_encriptada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           