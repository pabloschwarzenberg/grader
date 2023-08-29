#Aprobación de créditos
#ENTRADA
ingreso = int(input("ingrese el monto de su ingreso en pesos: "))
ano_nac = int(input("ingrese su año de  nacimineto: "))
num_hijos = int(input("ingrese cuantos hijos tiene: "))
anos_pertenencia_banco = int(input("ingrese cuantos años pertenece al banco: "))
estado_civil = input("ingrese su Estado civil ('S': soltero, 'C', casado): ").upper()
ciudad_campo = input("ingrese Si vive en campo o cuidad ('U': urbano, 'R': rural): ").upper()

#PROCESO
edad = 2021 - ano_nac 
#definimos la variable aprobado como 0, si cambia a 1 es poque se aprueba
aprobado = 0
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if (anos_pertenencia_banco > 10) and (num_hijos >= 2):
    aprobado=1
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif (estado_civil == "C") and (num_hijos > 3) and (45 < edad) and (edad < 55):
    aprobado=1
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif (ingreso > 2500000) and (estado_civil == "S") and  (ciudad_campo == "U"):
    aprobado=1
#si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif (ingreso > 3500000) and (anos_pertenencia_banco > 5):
    aprobado=1
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif (ciudad_campo == "R") and (estado_civil == "C") and (num_hijos < 2):
    aprobado=1

#SALIDA
if (aprobado == 1):
    print("APROBADO")
else:
    print("RECHAZADO")
      