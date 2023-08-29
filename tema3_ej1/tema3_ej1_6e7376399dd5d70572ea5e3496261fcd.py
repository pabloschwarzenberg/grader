# completa el código de la función
def suma_divisores(a):
    numero=[]
    for i in range(1,a):
        divisor=a%i
        if divisor ==0:
            numero.append(i)
        digito=sum(numero)
    if sum(numero)==1:
        return digito, True
    else:
        return sum(numero), False
           