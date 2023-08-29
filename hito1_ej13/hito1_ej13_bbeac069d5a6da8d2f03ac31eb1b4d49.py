#Definir si es primo o no
# 1=primo, 0=No primo
def EsPrimo(n):
    i = 2
    while n > i:
        if n/i == int(n/i) and n != 2:
            return 0
        i += 1
    return 1

#Entrada
Num = int(input("Ingrese un numero: "))

#Definir parametros
primos = []
i = 1

#Filtrado de numeros primos ultiles
while Num >= i:
    if EsPrimo(i) == 1:
        primos.append(i)
    i += 1

primos.remove(1)
factores=[]
i=0
while Num > 1 :
    if Num % primos[i] == 0:
        factores.append( primos[i] )               
        Num = int(Num / primos[i])
        i=0
    else:
        i+=1

#Salida
for T in factores:
    print(T)