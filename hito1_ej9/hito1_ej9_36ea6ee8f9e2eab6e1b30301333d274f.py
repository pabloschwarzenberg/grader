#Sistema de Ecuaciones
uno= int(input("primer numero: "))
dos= int(input("segundo numero: "))
tres= int(input("tercer numero: "))
cuatro= int(input("cuarto numero: "))
cinco= int(input("quinto numero: "))
seis= int(input("sexto numero: "))

denominador = uno*cinco - dos*cuatro

x= (tres*cinco - dos*seis) / denominador
y= (uno*seis - tres*cuatro) / denominador


print("x=",x,",","y=",y)
      