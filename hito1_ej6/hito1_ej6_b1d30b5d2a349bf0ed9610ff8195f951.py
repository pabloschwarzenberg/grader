#Ordenar tres números
a= int(input("Ingrese un numero: "))
b= int(input("Ingrese su suegundo numero: "))
c= int(input("Ingrese su tercer numero: "))

Min= min(a,b,c)
Max= max(a,b,c)

Medio= (a + b + c)- Min - Max

print("Su orden de menor a mayor es: ",Min,",",Medio,",",Max)