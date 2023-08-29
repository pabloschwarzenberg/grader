#Aprobación de créditos

# Entradas 
ingreso = int(input("Ingrese su sueldo en pesos: "))
ano_nacimiento  = int(input("Ingrese su año de nacimiento: "))
numero_de_hijos =  int(input("Ingrese el número de hijos: "))
anos_en_banco =  int(input("Ingrese el número de años en el banco: "))
estado_civil = str(input("Ingrese su estado civil (S): Soltero / (C) Casado: "))
campo_ciudad = str(input("Ingrese su zona de residencia (U): Urbano / (R) Rural: "))

# Variable para las validaciones
edad_cliente = 2021 - ano_nacimiento

#Proceso
## Si el cliente pertenece más de 10 años al banco y tiene dos o más hijos
if anos_en_banco > 10 and numero_de_hijos >= 2:
    print("APROBADO")

## Si el cliente es casado, tiene màs de tres hijos y tiene entre 45 y 55 años
elif estado_civil == 'C' and numero_de_hijos > 3 and edad_cliente >= 45 and edad_cliente <= 55:
    print("APROBADO")

#Si el cliente posee ingresos superiores a 2.500.000, es soltero y vive en la ciudad
elif ingreso>2500000 and estado_civil == 'S' and campo_ciudad =='C':
    print("APROBADO")

#Si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif ingreso > 3500000 and anos_en_banco > 5:
    print("APROBADO")

#Si el cliente vive en el campo, es casado y tiene menos de dos hijos
elif campo_ciudad == 'R' and estado_civil == 'C' and numero_de_hijos < 2:
    print("APROBADO")
    
else:
    print("RECHAZADO")
