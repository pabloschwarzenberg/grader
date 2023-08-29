a=int(input("Favor digite el primer numero: "))
b=int(input("Favor digite el segundo numero: "))
c=int(input("Favor digite el terecer numero: "))
x=min(a,b,c)
z=max(a,b,c)
y=(a+b+c)-x-z
print("Los numeros ordenados quedaron asi : {},{},{}".format(x,y,z))