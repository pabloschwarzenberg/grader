#Aprobación de créditos
#INGRESOS
ingreso = int(input("Inserte el ingreso en pesos: "))
if ingreso > 3500000:
    ingreso = 2

if ingreso > 2500000:
    ingreso = 1

#AÑO NACIMIENTO
Año_de_nacimiento = int(input("Año de nacimiento: "))
nacimiento = 2021 - Año_de_nacimiento 
if 45 <= nacimiento <=55:
    nacimiento = 1
else:
    nacimiento = 0

#NÚMERO DE HIJOS
Número_de_hijos = int(input("Número de hijos: "))
hijos = 0

while Número_de_hijos < 0:
    Número_de_hijos = int(input("Número de hijos: "))

if Número_de_hijos >= 2:
    hijos = 2
    
#AÑOS EN EL BANCO
Años_en_el_banco = int(input("Años de pertenencia al banco: "))
if Años_en_el_banco > 10:
    Años_en_el_banco = 2

elif Años_en_el_banco > 5:
    Años_en_el_banco = 1

elif Años_en_el_banco < 5:
    Años_en_el_banco = 0

#ESTADO CIVIL
Estado_civil = str(input("Estado civil soltero(S) o casado(C): "))
while Estado_civil != "S" and Estado_civil != "C":

    Estado_civil = str(input("Estado civil soltero (S) o casado (C): "))
    
if Estado_civil == "S":
    Estado_civil = 1

if Estado_civil == "C":
    Estado_civil = 0

#CAMPO O CIUDAD
Campo_o_ciudad = input("Si vive en campo (R) o ciudad (U): ")
while Campo_o_ciudad != "R" and Campo_o_ciudad != "U":
    Campo_o_ciudad = input("Si vive en campo (R) o ciudad (U): ")
    
if Campo_o_ciudad == "U":
    Campo_o_ciudad = 1

if Campo_o_ciudad == "R":
    Campo_o_ciudad = 0

n = 0

#CONDICIÓN 1.
if Años_en_el_banco == 2:
    if  hijos >= 2:
        print("APROBADO")
        n += 1

#CONDICIÓN 2.
elif Estado_civil == 0:
    if hijos == 3:
        if nacimiento == 1:
            print("APROBADO")
            n += 1
            
#CONDICIÓN 3.
elif ingreso >= 1:
    if Estado_civil == 1:
        if Campo_o_ciudad == 1:
            print("APROBADO")
            n += 1
            
#CONDICIÓN 4.
elif ingreso <= 2:
    if Años_en_el_banco >= 1:
        print("APROBADO")
        n += 1

#CONDICIÓN 5.
if Campo_o_ciudad == 0:
    if Estado_civil == 0:
        if hijos <= 1:
            print("APROBADO")
            n += 1

if n == 0:
    print("RECHAZADO")
