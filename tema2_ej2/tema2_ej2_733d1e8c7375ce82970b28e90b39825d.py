# completa el código de la función
def amigos(a,b):
    suma_div_a=[0]
    suma_div_b=[0]
    #calcular suma de divisores de a
    for i in range(1,a):
        if a%i==0:
            suma_div_a[0]+=i
    #calcular suma de divisores de b
    for i in range(1,b):
        if b%i==0:
            suma_div_b[0]+=i
    #comprobar si son numeros amigos
    if  suma_div_a[0]==b and suma_div_b[0]==a:
        return True
    else:
        return False
           