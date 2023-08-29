def buscarTodas(a,b):
    lista=[]
    lista_1=[]
    cont=0

    for i in a:
        if i==b:
            lista.append(cont)
        cont+=1
    for i in lista:
        lista_1.append(str(i))
    #print(" ".join(lista_1))
    #para que una función retorne un valor debes usar return no print
    #en general una función no debe contener ni input ni print
    #porque debe estar preparada para funcionar en cualquier parte del programa
    #y debe recibir lo que necesita para funcionar de sus parámetros
    #y entregar su resultado con return
    #o sea:
    return " ".join(lista_1)

if __name__ == "__main__":
    a=input("Inserte frase cualquiera:")
    b=input("Inserte letra a buscar en la frase anterior:")
    buscarTodas(a,b)
