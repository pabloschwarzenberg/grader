#Ordenar tres números
x= int(input("Ingresar primer numero: "))
y= int(input("Ingresar segundo numero: "))
z= int(input("Ingresar tercer numero: "))

Min= min(x,y,z)
Max= max(x,y,z)

Medio= (x + y + z)- Min - Max

print("Orden de menor a mayor es: ",Min,",",Medio,",",Max)