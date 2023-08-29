def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyz"
    encript = abc[13:] + abc[:13]
    lista = []
    for l in palabra:
        lista.append(l)
    listaEncriptada = []
    for pos in range(len(lista)):
        num = abc.find(lista[pos])
        letra = encript[num]
        listaEncriptada.append(letra)
    encriptada = ""
    for letra in listaEncriptada:
        encriptada += letra

    return encriptada
        
        
if __name__ == "__main__":
    palabra = input("ingrese la palabra para encriptarla: ")
    palabra.lower()
    rot13(palabra)
    respuesta = rot13(palabra)
    print("El resultado es: ", respuesta)
           