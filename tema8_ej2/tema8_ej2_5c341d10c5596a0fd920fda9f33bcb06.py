def buscarTodas(frase,letra):
    frase=str(frase)
    letra=str(letra)
    contador=0
    busquedas=0
    lista=[]
    while contador<1:
        numero=frase.find(letra,busquedas)
        if numero>=0:
            lista.append(numero)
            lista.append(" ")
            busquedas=numero+1
        else:
            contador=contador+1
    numero2=len(lista)-1
    numero2=int(numero2)
    lista.pop(numero2)
    palabra="".join(str(e)for e in lista)    
    return palabra
if __name__ == "__main__":
    print("Ingrese la frase y la letra que desea utilizar: ")
    a=input("Frase: ")
    b=input("Letra: ")
    resultado=buscarTodas(a,b)
    print(resultado)

