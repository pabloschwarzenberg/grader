#Ordenar tres números
a=input("Ingrese numero: ")
b=input("Ingrese numero: ")
c=input("Ingrese numero: ")
if a>=b>=c:
   print("De menor a mayor",c,",",b,",",a)
if b>=a>=c:
   print("De menor a mayor",c,",",a,",",b)
if c>=b>=a:
   print("De menor a mayor",a,",",b,",",c)
if a>=c>=b:
   print("De menor a mayor",b,",",c,",",a)
if b>=c>=a:
   print("De menor a mayor",a,",",c,",",b)    

