#Ordenar tres números
o=int(input("ingrese un numero par:"))
t=int( input("ingrese un segundo numero par:"))
e=int(input("ingrese un tercer numero par:"))
a=min(o,t,e)
c=max(o,t,e)
b=(o+t+e)-a-c
print("los numeros ordenados quedan asi:{},{},{}".format(a,b,c))