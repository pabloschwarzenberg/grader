#Ordenar tres números
x=eval(input('primer numero:'))
y=eval(input('segundo numero:'))
z=eval(input('tercer numero:'))

a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print('el orden de los numeros es:',(a,b,c))