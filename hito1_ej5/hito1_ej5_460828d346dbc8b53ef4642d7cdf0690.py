#Cálculo del dígito verificador de un rut
import os
import math
#dv=0
numero = int (input ('Ingresa el valor de numero: '))


n9=((numero%1000000000-numero%100000000)//100000000)*4
n8=((numero%100000000-numero%10000000)//10000000)*3
n7=((numero%10000000-numero%1000000)//1000000)*2
n6=((numero%1000000-numero%100000)//100000)*7
n5=((numero%100000-numero%10000)//10000)*6
n4=((numero%10000-numero%1000)//1000)*5
n3=((numero%1000-numero%100)//100)*4
n2=((numero%100-numero%10)//10)*3
n1=(numero%10)*2
suma=n1+n2+n3+n4+n5+n6+n7+n8+n9
dividir= math.trunc(suma/11)
resto=(suma-(11*dividir))
resultado=(11-resto)


if resultado==11:
    dv=0
elif(resultado==10):
    dv="k"
else:
    dv=resultado

print(dv)

