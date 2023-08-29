def rot13(palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    transformar = abecedario[13:]+abecedario[:13]
    rot_abc = lambda i: transformar[abecedario.find(i)]\
        if abecedario.find(i) >-1 else i
    return ''.join(rot_abc(i) for i in palabra)
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           