#Ejercicio Suma de Divisores
#Hitos 2, Ejercicio 1.

from operator import truediv


def suma_divisores(a):
    div=[i for i in range(1,a)
    if a%i==0]
    m=sum(div)
    if m==1:
        return m,True
    return m,False