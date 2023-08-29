def cambiar_letra(letra):
    if ord(letra) <= ord("m"):
        return chr(ord(letra)+13)
    else:
        return chr(ord(letra)-13)
        
def rot13(palabra):
    resultado = ""
    for i in range(len(palabra)):
        resultado += cambiar_letra(palabra[i])
    return resultado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           