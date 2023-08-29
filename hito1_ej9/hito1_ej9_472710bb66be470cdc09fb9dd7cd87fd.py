i = float(input("ingrese el valor de a: "))
h = float(input("ingrese el valor de b: "))
g = float(input("ingrese el valor de c: "))
d = float(input("ingrese el valor de d: "))
e = float(input("ingrese el valor de e: "))
f = float(input("ingrese el valor de f: "))

if i/d==h/e and h/e==g/f :

   print("TIENE MUCHAS SOLUCIONES")
   
elif  i/d==h/e  and h/e!=g/f :

   print("NO HAY SOLUCION")
   
else :  
    x = (g*e-f*h)/(i*e-d*h)
    y = (i*f-d*g)/(i*e-d*h)
    
    print("x=" , round(x,1))
    
    print("y=" , round(y,1))

 
