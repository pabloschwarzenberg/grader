def buscarTodas(a,b): 
    contador = 0 
    lista = list(a)
    acumulador = ""
    for letras in a:
        if lista[contador] == b:

            acumulador += str(contador) + " "
        contador +=  1
    x = list(acumulador)
    lenLista = len(x)
    del x[lenLista - 1]
    x = "".join(x)
    return(x)

if __name__ == "__main__":
    palab = str(input("palabra: "))
    letra = str(input("letra: "))
    print(buscarTodas(palab,letra))
           