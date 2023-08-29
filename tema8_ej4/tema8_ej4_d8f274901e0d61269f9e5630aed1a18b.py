def rot13(palabra):
    #Abcdario
    letras = "abcdefghijklmnopqrstuvwxyz"
    #Contador verificador
    contador = palabra.count("abcdefghijklmnopqrstuvwxyz")
    condicion = False
    while condicion == True:
        if int(contador) < 1:
            Exception("Texto invalido")
            False
        else:
            True
            pass
    #ROT13 fuction char x char
    mover = letras[13:]+letras[:13]
    buscar = lambda i: mover[letras.find(i)] if letras.find(i)>-1 else i
    return ''.join( buscar(i) for i in palabra)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           