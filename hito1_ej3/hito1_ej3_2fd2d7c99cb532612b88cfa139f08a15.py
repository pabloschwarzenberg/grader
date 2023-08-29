#Aprobación de créditos
Ingreso=int(input("Ingreso: $"))
Año=int(input("Ingrese su año de nacimiento: "))
while not (Año>=1900 and Año<=2020):
    Año=int(input("Ingrese un año valido para su nacimiento: "))
Hijos=int(input("Cantidad de hijos: "))
AñosBanco=int(input("Ingrese la cantidad de años que lleva en el banco: "))
EstadoCivil=input("Ingrese su estado Civil S:Soltero ; C:Casado : ")
while not (EstadoCivil=="S" or EstadoCivil=="C"):
    EstadoCivil=(input("Ingrese una de las opciones S:Soltero ; C:Casado : "))
CampoCiudad=(input("Ingrese la zona donde vive U:Urbana ; R:Rural : "))
while not (CampoCiudad=="U" or CampoCiudad=="R"):
    CampoCiudad=input("Ingrese una de las opciones U:Urbana ; R:Rural : ")
edad=2020-Año
if (AñosBanco >10 and Hijos>=2):
    print("APROBADO")
elif (EstadoCivil=="C" and Hijos>3 and edad<=55):
      print("APROBADO")
elif Ingreso>2500000 and EstadoCivil=="S" and CampoCiudad=="U":
    print("APROBADO")
elif (Ingreso > 3500000 and AñosBanco>5):
    print("APROBADO")
elif (CampoCiudad=="R" and EstadoCivil=="C" and Hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")