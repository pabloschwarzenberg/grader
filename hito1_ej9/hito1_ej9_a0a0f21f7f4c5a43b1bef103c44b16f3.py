#Sistema de Ecuaciones
      #ax + by = c
#dx + ey = f

def sistema(a,b,c,d,e,f):
      determinante = a*e - b*d

      if determinante != 0:
            x = (c*e - b*f)/determinante
            y = (a*f - c*d)/determinante
            print("x = ",x)
            print("y = ",y)
      else:
            print("no tiene solucion")
            
print("ijiste valores para a,b,c,d,e,f")
a = float(input("valor de a:"))
b = float(input("valor de b:"))
c = float(input("valor de c:"))
d = float(input("valor de d:"))
e = float(input("valor de e:"))
f = float(input("valor de f:"))

sistema(a,b,c,d,e,f)