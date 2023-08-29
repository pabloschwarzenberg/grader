#Ordenar tres números
a=int(input("Escriba el Primer Numero:"))
b=int(input("Escriba el Segundo Numero:"))
c=int(input("Escriba el Tercer Numero:"))
x=min(a,b,c)
y=max(a,b,c)
z=(a+b+c)-x-y
print("Los Numeros son",(x,z,y))