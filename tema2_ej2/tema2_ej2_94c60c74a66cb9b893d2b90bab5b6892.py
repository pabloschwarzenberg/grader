# completa el código de la función
#dos numeros son amigos si la suma de los divisores de uno de ellos es igual al otro numero y viceversa 
#(el calculo de los divisores no consideran al mismo numero)
def amigos(a,b):
    valor = False
    sumaa=0
    sumab=0

    for i in range(1,a): #suma de los divisores de a, exceptuando a "a"
        if(a % i) == 0: sumaa = sumaa + i
    
    for i in range(1,b): #suma de los divisores de b, exceptuando a "b"
        if(b % i) == 0: sumab = sumab + i

    if(sumaa==b and sumab==a) : valor = True

    return valor
           