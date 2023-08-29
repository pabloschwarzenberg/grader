#cifrado coloca la letra que va 13 posiciones adelante
def rot13(palabra):
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    lista_abc = list(abecedario)
    lista_palabra=list(palabra)
    for i in range(0,len(lista_palabra)):
        for x in range(0,len(lista_abc)):
            if lista_palabra[i]==lista_abc[x]:
                if x<=12:
                    lista_palabra[i]=lista_abc[x+13]
                elif x>12:
                    lista_palabra[i]=lista_abc[x-13]
                break


    palabra="".join(lista_palabra)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)