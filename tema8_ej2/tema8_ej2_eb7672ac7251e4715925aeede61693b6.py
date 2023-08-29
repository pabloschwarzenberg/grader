def buscarTodas(a,b):
    v=1
    Lpalabra=list(a)
    apariciones=[]
    i=0
    while i<=((len(a))-1):
        if Lpalabra[i]==b:
            apariciones.append(" ")
            apariciones.append(str(i))


        else:
            pass
        i = i + 1


    apariciones.remove(" ")


    resultado="".join(apariciones)
    return resultado

        

if __name__ == "__main__":
    pass
           