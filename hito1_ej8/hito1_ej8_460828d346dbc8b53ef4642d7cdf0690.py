import os
numero=[]
numero = int (input ('Ingresa el valor de numero: '))
m=(numero%10000-numero%1000)//1000
c=(numero%1000-numero%100)//100
d=(numero%100-numero%10)//10
u=numero%10
unidades=['M','C','D','U']
print (m,unidades[0],"+", c,unidades[1],"+", d,unidades[2],"+", u,unidades[3])