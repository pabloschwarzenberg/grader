#Ordenar tres números
x=int(input("Escriba Un Primer Numero"))
y=int(input("Escriba Un Segundo Numero"))
z=int(input("Escriba Un Tercer Numero"))

a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c

print("Los Numeros De Menor a Mayor son: {},{},{}".format(a, b, c))