#Aprobacion de creditos
S = "soltero"
C = "casado"
U = "urbano"
R = "rural"


ingreso =int(input("Ingrese ingreso monetario(pesos): "))
añoDeNacimiento = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos: "))
añosDePertenencia = int(input("Ingrese años de pertenecia al banco: "))
estadoCivil = input("Ingrese estado civil (S:soltero, C:casado): ")
vivienda = input("Ingrese zona de vivienda(U:urbano, R:rural): ")

edad = 2020 - añoDeNacimiento

if añosDePertenencia > 10 and hijos >= 2:
    print("APROBADO")
    
elif estadoCivil == C and hijos >= 3 and edad >= 45 and edad <= 55:   
      print("APROBADO")
    
elif ingreso > 2500000 and estadoCivil == "S" and vivienda == "U":
      print("APROBADO")
    
elif ingreso > 3500000 and añosDePertenencia > 5:
      print("APROBADO")
    
elif vivienda == "R" and estadoCivil == "C" and hijos < 2:
      print("APROBADO")
      
else:
    print("RECHAZADO")
