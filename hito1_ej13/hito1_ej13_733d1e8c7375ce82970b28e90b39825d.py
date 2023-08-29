def es_primo(numero):
    numeros=[2,3,4,5,6,7,8,9]
    if  numero==1:
        return False
    for i in numeros:
        if i==numero:
            numeros.remove(i)
    for i in numeros:
        if numero%i==0:
            return False
    if numero%numero==0 and numero%1==0:
        return True

def fac_primos(numero):
    #hacer lista de numeros primos en el rango del numero
    n_primos=[]
    f_primos=[]
    for i in range(numero):
        n=es_primo(i)
        if n==True:
            n_primos.append(i)
    #revisar factores primos
    for i in n_primos:
        if numero%i==0:
            f_primos.append(i)
            numero//=i
    f_primos.append(numero)
    for i in f_primos:
        if  i==1:
            f_primos.remove(i)      
    #retornar lista de factores primos
    return f_primos
            
#entrada
num=int(input("Ingrese número: "))
#crear lista de factores primos
fPrimos_calculados=fac_primos(num)
#imprimir factores primos
for i in fPrimos_calculados:
    print(i)