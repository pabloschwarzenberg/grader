#Factores Primos
def es_primo(numero):
    divisor=2
    esprimo=True
    while esprimo and divisor<=numero/2:
        if numero%divisor==0:
            esprimo=False
        divisor+=1
    if esprimo==True:
        return True
    else:
        return False



def fact(num):
    factores=[]
    divisor=2
    while divisor<=num/2:
        if numero%divisor==0:
            factores.append(divisor)
        if divisor**2==numero:
            factores.append(divisor)
        divisor+=1
    return factores



simp=[]
numero=int(input("ingrese numero entero: "))
divisor=2
if es_primo(numero)==True:
    print(numero)
else:
    factores=fact(numero)
    factores1=fact(numero)
    t=0
    while t<len(factores):
        if factores[t]**2 in factores1:
            factores1.append(factores[t])
        t+=1
    i=0
    while i<len(factores1):
        if es_primo(factores1[i])==True:
            print(factores1[i])
        i+=1