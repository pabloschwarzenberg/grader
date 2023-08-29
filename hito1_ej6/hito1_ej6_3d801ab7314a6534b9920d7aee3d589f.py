#forma2 misma linea separado por comas
x=int(input("esciba el primer numero:"))
y=int(input("esciba el segundo numero:"))
z=int(input("esciba el tercer numero:"))

a=min(x,y,z)
c=max(x,y,z)
b=(x+y+z)-a-c
print("los numeros ordenados son:{},{},{}".format(a,b,c))