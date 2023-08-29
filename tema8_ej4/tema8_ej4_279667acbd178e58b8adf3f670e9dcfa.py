def rot13(palabra):
    abecedario1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    abecedario2 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string = ''
    for letra in palabra:
        for posicion,abcd in enumerate(abecedario1):
            if letra == abcd:
                string += abecedario2[posicion]
        for posicion,abcd in enumerate(abecedario2):
            if letra == abcd:
                string += abecedario1[posicion]
    return(string)
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra = palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           