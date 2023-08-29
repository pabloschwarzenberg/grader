def descomponerNumero(numero):
    descomposicion=[]
    indice=1
    while numero!=0:
        dig= str(numero%10)
        if indice==1:
            descom= dig+"U"
            descomposicion.append(descom)
        elif indice==2:
            descom= dig+"D"
            descomposicion.append(descom)
        elif indice==3:
            descom= dig+"C"
            descomposicion.append(descom)
        elif indice==4:
            descom= dig+"M"
            descomposicion.append(descom)
        indice+=1
        numero//=10
    lista=reversed(descomposicion)
    return lista
def mostrarDescomposicion(numero):
    lista= descomponerNumero(numero)
    indice =0
    for digito in lista:
        if indice==0:
            print(digito,end=" ")
        else:
            print("+",digito,end=" ")
        indice+=1
numero=int(input())
mostrarDescomposicion(numero)