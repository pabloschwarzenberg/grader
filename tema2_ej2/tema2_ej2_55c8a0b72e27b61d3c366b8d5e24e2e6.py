def amigos(numero1,numero2):
    suma1=0
    for i in range(1,numero1):
        if numero1%i==0:
            suma1=suma1+i
    suma2=0
    for i in range(1,numero2):
        if numero2%i==0:
            suma2=suma2+i
    if(suma1==numero2 and suma2==numero1):
        return True
    else:
        return False

           