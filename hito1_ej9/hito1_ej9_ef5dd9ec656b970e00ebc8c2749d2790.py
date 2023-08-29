#Sistema de Ecuaciones

#ENTRADA

a = float(input("Ingrese termino a: "))
b = float(input("Ingrese termino b: "))
c = float(input("Ingrese termino c: "))
d = float(input("Ingrese termino d: "))
e = float(input("Ingrese termino e: "))
f = float(input("Ingrese termino f: "))

determinante = a*e - b*d

if determinante > 0:
        x = (c*e -b*f)/ determinante
        y = (a*f - c*d)/ determinante
        x = round(x,1)
        y = round(y,1)
        
#DESARROLLO

        print("x = ",x)
        print("y = ",y)

      