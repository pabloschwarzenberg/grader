# por favor escribe aquí tu función
def es_primo(numero):
    contador=0
    for i in range(1,(numero+1)):
        #print(i)
        if numero%i==0:
            contador=contador+1
            print(contador)
    if contador>2:
        resultado=False
    else:
        resultado=True
        if numero==1:
            resultado=False
    return resultado



           