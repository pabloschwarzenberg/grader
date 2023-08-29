def solucion(a,b,c,d,e,f):
    det= a*e - b*d
    if det !=0:
        x= (c*e - b*f)/det
        y= (a*f - c*d)/det
        
        print("x=", x, "y=",y)
    else:
          return None, None
a = int(input("Ingresa numero 1:"))
b = int(input("Ingresa numero 2:"))
c= int(input("Ingresa numero 3:"))
d= int(input("Ingresa numero 4:"))
e= int(input("Ingresa numero 5:"))
f= int(input("Ingresa numero 6:"))
print(solucion(a,b,c,d,e,f))
      