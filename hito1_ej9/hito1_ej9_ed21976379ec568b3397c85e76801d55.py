a=int(input("ingresa A:"))
b=int(input("ingresa B:"))
c=int(input("ingresa C:"))
d=int(input("ingresa D:"))
e=int(input("ingresa E:"))
f=int(input("ingresa F:"))

determinar=((a*e)-(b*d))

    
if(determinar!=0):
    x=((c*e)-(b*f))/determinar
    print("x=",x)
    y=((a*f)-(c*d))/determinar
    print("y=",y)
        
        
else:
    print("no tiene solucion")