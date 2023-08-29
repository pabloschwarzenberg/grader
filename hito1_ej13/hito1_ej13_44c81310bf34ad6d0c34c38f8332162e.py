#Factores Primos
def descomposicion(x):
    lista=[]
    for i in range(2,x+1):
        while x % i == 0:
            lista.append(i)
            x = x / i
    return lista
x=int(input('ingrese un numero:'))
r=(descomposicion(x))
for i in zip(r):
    print(' '.join(map(str,i)))      