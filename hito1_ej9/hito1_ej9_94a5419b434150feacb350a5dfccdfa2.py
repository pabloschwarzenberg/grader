#Sistema de Ecuaciones
#primer sistema
print("Primer sistema")
x=float(input("Escriba su primer variante x= "))
y=float(input("Escriba su segunda variante y= "))
z=float(input("Escriba su tercer variante z= "))

#Segundo sistema
print("Segundo sistema")
X=float(input("Escriba su primer variante X= "))
Y=float(input("Escriba su segunda variante Y= "))
Z=float(input("Escriba su tercer variante Z= "))

#Se= x + y = z
#Se2= X + Y = Z

xX = (z*Y - y*Z) // (x*Y - y*X)
yY = (x*Z - z*X) // (x*Y - y*X)

print("x= %5.1f" "y=%5.1f" %(xX, yY))
