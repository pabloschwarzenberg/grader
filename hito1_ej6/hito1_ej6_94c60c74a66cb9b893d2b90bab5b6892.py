# ordenar tres numeros de menos a mayor separados por una coma.
x=int(input("escriba el primer numero: "))
y=int(input("escriba el segundo numero: "))
Z=int(input("escriba el tercer numero: "))

a=min(x,y,Z)
c=max(x,y,Z)
b=(x+y+Z)-a-c


print("los numeros ordenados de menor a mayor son: {}, {}, {} ".format(a,b,c))


      