x=int(input("Escribe el primer numero: "))
y=int(input("Escribe el segundo numero: "))
z=int(input("Escribe el tercer numero: "))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("Los numeros ordenados son:",(a ,b, c))