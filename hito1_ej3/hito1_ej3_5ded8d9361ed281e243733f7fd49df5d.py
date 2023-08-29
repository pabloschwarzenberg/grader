respuesta = "RECHAZADO"

ingresos = int(input("Ingreso Total en Pesos: "))
                 
nacimiento = int(input("Año de Nacimiento: "))

ano = 2022

edad = (ano - nacimiento)
                 
hijos = int(input("Número de Hijos: "))
                 
pertenencia = int(input("Años de Pertenencia en el Banco: "))
                 
estado_civil = input("Estado Civil, S = Soltero, C = Casado: ")
        
vive = input("¿vive en el Campo o la Ciudad? U = Ubano, R = Rural: ")

if pertenencia >= 10 and hijos >= 2:
  respuesta = "APROBADO"

if estado_civil == "C" and hijos > 3 and edad >= 45 and edad <= 55:
  respuesta = "APROBADO"

if ingresos > 2500000 and estado_civil == "S" and vive == "U":
  respuesta = "APROBADO"

if ingresos > 3500000 and pertenencia > 5 :
  respuesta = "APROBADO"

if vive == "R" and estado_civil == "C" and hijos < 2:
  respuesta = "APROBADO"

print (respuesta)
