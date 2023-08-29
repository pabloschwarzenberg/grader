print("los numeros se ordenaran de menor a mayor")
x =eval(input("ingrese primer numero:"))
y=eval(input("ingrese segundo numero:"))
z=eval(input("ingrese tercer numero:"))
a=min(x,y,z)
b=max(x,y,z)
c= (x+y+z) -a -b

print("los numeros son:{},{},{}".format(a,c,b))