def numero_perfecto(a):
    numero=[]
    for i in range(1,a):
        divisor=a%i
        if divisor ==0:
            numero.append(i)
        digito=sum(numero)
    if digito==a:
        return True
        
    else:
        return False