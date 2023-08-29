# completa el código de la función
def suma_divisores(a):
    numero=a
    sumaDivisores=0
    divisores=1
    verdad=False
    while divisores<numero:
        if numero%divisores==0:
            sumaDivisores+=divisores
        divisores+=1
    if sumaDivisores==1:
        verdad=True
    return (sumaDivisores,verdad)
           