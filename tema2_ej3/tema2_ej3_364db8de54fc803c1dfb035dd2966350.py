#numero perfecto
def numero_perfecto(b):
    divisores=[1]
    for n in range(2,b):
        if b%n==0:
            divisores.append(n)
    suma=sum(divisores)    
    if b==suma:
        return True
    else:
        return False