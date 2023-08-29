#Aprobación de créditos
#declaracion variables de ingreso
ingreso = int(input("inserte el ingreso en pesos "))
if ingreso > 300000:
    ingreso = 2
    
if ingreso > 300000:
    ingreso = 1
    
#declaracion variables de nacimiento    
año_de_nacimiento = int(input("año de nacimiento: "))
nacimiento = 2021 - año_de_nacimiento 
if 45 <= nacimiento <=55:
    nacimiento = 1
else:
    nacimiento = 0

#declaracion variables de hijos
hijos_respaldo = int(input("numero de hijos: "))
hijos = 0

if hijos_respaldo >= 2:
    hijos = 2
    if hijos_respaldo > 3:
        hijos = 3
    
if hijos_respaldo < 2:
    hijos = 1

if hijos_respaldo == 0:
    hijos = 0

#declaracion variables de años_en_banco
años_en_banco = int(input("años de pertenencia al banco: "))
if años_en_banco > 10:
    años_en_banco = 4
    
elif años_en_banco > 5:
    años_en_banco = 1
    
elif años_en_banco < 5:
    años_en_banco = 2

#declaracion variables estado_civil
estado_civil = str(input("estado civil S o C: "))

if estado_civil == "S":
    estado_civil = 1
    
if estado_civil == "C":
    estado_civil = 0



#declaracion variables campo_o_ciudad
campo_o_ciudad = input("si vive en campo(R) o ciudad(U): ")

if campo_o_ciudad == "U":
    campo_o_ciudad = 0
    
if campo_o_ciudad == "R":
    campo_o_ciudad = 1

print(ingreso, nacimiento, hijos, años_en_banco, estado_civil, campo_o_ciudad)

n = 0



#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if años_en_banco == 2 and hijos >= 2:
        print("APROBADO")
        n += 1

#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.       
elif estado_civil == 0 and hijos == 3 and nacimiento == 1:
            print("APROBADO")
            n += 1
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif ingreso >= 1 and estado_civil == 1 and campo_o_ciudad == 1:
    print("APROBADO")
    n += 1

#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif ingreso <= 2 and años_en_banco >= 1:
        print("APROBADO")
        n += 1

#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
if campo_o_ciudad == 0 and estado_civil == 0 and hijos <= 1:
    print("APROBADO")
    n += 1

if n == 0:
    print("RECHAZADO")      