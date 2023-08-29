#Aprobación de créditos
ingreso = int(input("inserte el ingreso en pesos "))
if ingreso > 3500000:
    ingreso = 2
    
if ingreso > 2500000:
    ingreso = 1
        
año_de_nacimiento = int(input("año de nacimiento: "))
nacimiento = 2021 - año_de_nacimiento 
if 45 <= nacimiento <=55:
    nacimiento = 1
else:
    nacimiento = 0

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

años_en_banco = int(input("años de pertenencia al banco: "))
if años_en_banco > 10:
    años_en_banco = 2
    
elif años_en_banco > 5:
    años_en_banco = 1
    
elif años_en_banco < 5:
    años_en_banco = 0

estado_civil = str(input("estado civil S o C: "))

if estado_civil == "S":
    estado_civil = 1
    
if estado_civil == "C":
    estado_civil = 0
    
campo_o_ciudad = input("si vive en campo(R) o ciudad(U): ")

if campo_o_ciudad == "U":
    campo_o_ciudad = 1
    
if campo_o_ciudad == "R":
    campo_o_ciudad = 0

print(ingreso, nacimiento, hijos, años_en_banco, estado_civil, campo_o_ciudad)

n = 0

if años_en_banco == 2 and hijos >= 2:
        print("APROBADO")
        n += 1
  
elif estado_civil == 0 and hijos == 3 and nacimiento == 1:
            print("APROBADO")
            n += 1

elif ingreso >= 1 and estado_civil == 1 and campo_o_ciudad == 1:
    print("APROBADO")
    n += 1

elif ingreso <= 2 and años_en_banco >= 1:
        print("APROBADO")
        n += 1

if campo_o_ciudad == 0 and estado_civil == 0 and hijos <= 1:
    print("APROBADO")
    n += 1

if n == 0:
    print("RECHAZADO") 