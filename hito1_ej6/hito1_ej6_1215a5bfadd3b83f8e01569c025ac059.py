#Ordenar tres números
x=int(input("favor digite el primer numero: "))
y=int(input("favor digite el segundo numero: "))
z=int(input("favor digite el tercer numero: "))
a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("los numeros quedan de la sgte manera {},{},{}".format(a,b,c))