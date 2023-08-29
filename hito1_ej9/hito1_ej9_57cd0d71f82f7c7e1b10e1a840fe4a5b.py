print("ingrese los siguientes valores: ")
#primer sistema 
print("primer sistema: ax+by=c")
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))
#segundo sistema 
print("segundo sistema: dx+ey=f")
d=float(input("d= "))
e=float(input("e= "))
f=float(input("f= "))
#desarrollo
x=(((c*e)-(b*f))/((a*e)-(b*d)))
y=(c-a*x)/b
print("x= ",x)  
print("y= ",y)