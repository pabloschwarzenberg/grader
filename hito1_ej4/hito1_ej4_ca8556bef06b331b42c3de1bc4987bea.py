#Conversión de Decimal a Binario
from random import choice
num= int(input("Ingrese valor de n: "))

def funcionB(x):
    a= x.replace("0","x")
    b= a.replace("1","0")
    c= b.replace("x","1")
    return c

print(funcionB(num))
