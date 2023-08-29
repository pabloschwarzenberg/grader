#Aprobación de Créditos
from datetime import date 
  
def Edad(nacimiento): 
    hoy = date.today() 
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day)<(nacimiento.month, nacimiento.day)) 
    return edad 

#Variables
ingreso = int(input("Ingrese sus ingresos anuales en pesos: "))
diaX = int(input("Ingrese fecha de nacimiento en numeros\nDía: "))
mesX = int(input("Mes: "))
anioX = int(input("Año: "))
hijos = int(input("Ingrese numero de hijos:  "))
pertenencia = int(input("¿Cuantos años lleva perteneciendo al banco? "))
print("Ingrese su estado civil de la siguiente forma")
estado = input("S: Soltero\nC: Casado\nEstado Civil: ")
print("Ingrese el tipo de vivienda al que pertenece de la siguiente forma")
vivienda = input("U: Urbano\nR: Rural\nVivienda: ")
Edad(date(anioX,mesX,diaX))

#Decisiones
if pertenencia >= 10 and hijos >=2:
    credito='Aprobado'
elif estadoCivil == 'C' and hijos >=3 and edad >=45 and edad <55:
    credito='Aprobado'
elif ingreso > 2500000 and estadoCivil == 'S' and vivienda == 'U':
    credito='Aprobado'
elif ingreso > 3500000 and pertenencia >=5:
    credito=='Aprobado'
elif vivienda == 'R' and estadoCivil == 'C' and hijos < 2:
    credito='Aprobado'
else:
    credito='Rechazado'
print(credito)