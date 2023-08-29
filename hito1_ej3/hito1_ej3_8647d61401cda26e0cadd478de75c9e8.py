from datetime import date 
  
def Edad(nacimiento): 
    hoy = date.today() 
    edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day)<(nacimiento.month, nacimiento.day)) 
    return edad 

ingreso = int(input("Ingrese sus ingresos anuales en pesos: "))
diaX = int(input("Ingrese fecha de nacimiento en numeros\nDía: "))
mesX = int(input("Mes: "))
anioX = int(input("Año: "))
hijos = int(input("¿Cuantos hijos tiene? "))
pertenencia = int(input("¿Cuantos años lleva perteneciendo al banco? "))
estadoCivil = input("Estado civil\nIngrese su estado civil de la siguiente forma")
print("S: Soltero\nC: Casado")


print(Edad(date(2001, 8, 10)), "años")
