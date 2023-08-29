#Sistema de Ecuaciones
c1 = int(input(" ingrese el numero del valor a :"))
c2 = int(input(" ingrese el numero del valor b :"))
c3 = int(input(" ingrese el numero del valor c :"))
c4 = int(input(" ingrese el numero del valor d :"))
c5 = int(input(" ingrese el numero del valor e :"))
c6 = int(input(" ingrese el numero del valor f : "))

proceso1 = (c5)*(c1)-(c2)*(c4)

prosesoX = (c5)*(c3)-(c2)*(c6)
prosesoY = (c6)*(c1)-(c3)*(c4)

solucionX = prosesoX/proceso1
solucionY = prosesoY/proceso1

print ("y = " , solucionY )
print ("x = " , solucionX )