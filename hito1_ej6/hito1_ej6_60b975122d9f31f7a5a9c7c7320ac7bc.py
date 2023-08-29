#Ordenar tres números
V1=int(input('ingresar variable 1:'))
V2=int(input('ingresar variable 2:'))
V3=int(input('ingresar variable 3:'))

a=min(V1,V2,V3)
c=max(V1,V2,V3)
b=(V1+V2+V3)-a-c
print('el orden de los numeros es:',(a,b,c))



