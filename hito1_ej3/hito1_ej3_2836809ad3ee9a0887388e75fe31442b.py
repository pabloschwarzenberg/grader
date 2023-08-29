Ingreso=int(input("Ingreso: $"))
nacimiento=int(input("Ingrese su año de nacimiento: "))
while not (Año>=1900 and Año<=2020): 
nacimiento=int(input("Ingrese un año valido para su nacimiento: ")) 
Hijos=int(input("Cantidad de hijos: ")) 
tiempoBanco=int(input("Ingrese la cantidad de años que lleva en el banco: "))
EstadoCivil=input("Ingrese su estado Civil S:Soltero ; C:Casado : ") 
while not (EstadoCivil=="S" or EstadoCivil=="C"): 
EstadoCivil=str(input("Ingrese una de las opciones S:Soltero ; C:Casado : "))
CampoCiudad=(input("Ingrese la zona donde vive U:Urbana ; R:Rural : ") 
while not (CampoCiudad=="U" or CampoCiudad=="R"):
CampoCiudad=str(input("Ingrese una de las opciones U:Urbana ; R:Rural : "))
