def numero_perfecto(a):
    contador = a - 1
    valor = 0
    x = a
    contador = a - 1
    condicion = False
    while(contador>0):
        if(x%contador == 0):
            valor = valor + contador
        contador = contador - 1
    if(valor ==  a):
        condicion = True
    return condicion

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
