#Aprobación de créditos
      #modulos.
from colorama import Style, Back, Fore, init

#correccion de cmd.
init(convert=True)

#variables.
ingresos = input("ingrese sus ingresos: $")
año_nacimiento = input("ingrese su año de nacimiento: ")
numero_hijos = input("ingrese cuantos hijos tiene: ")
año_banco = input("ingrese cuantos años lleva en el banco: ")

#variables con letras.
estado_civil = input("ingrese su estado civil, \"S\": para soltero, \"C\": para casado: ")
vivienda = input("ingrese el lugar donde vive \"U\": para Urbano , \"R\":para Rural: ")


try:
    #confirmacion de mayus.
    estado_civil = estado_civil.upper()
    vivienda = vivienda.upper()
    
    #confirmacion de letras.
    if estado_civil == "C" or estado_civil == "S":
        if vivienda =="U" or vivienda == "R":
            print(Fore.GREEN + "Valores Validos.")
            valor = True
    else: 
        print(Fore.RESET + 20*"-")
        print(Fore.RED + "ERROR:")
        print(Fore.RED + "fallo al ingresar la letra.")
        exit()

except ValueError:
    print(Fore.RESET + 20*"-")
    print(Fore.RED + "ERROR:")
    print(Fore.RED + "fallo al ingresar la letra.")
    exit()

#confirmacion de numeros.
try:
    #redondeo de numeros.
    ingresos = int(ingresos)
    año_nacimiento = int(año_nacimiento)
    numero_hijos = int(numero_hijos)
    año_banco = int(año_banco)
    
    print(Fore.RESET + 20*"-")
    if valor != True:
        print(Fore.GREEN + "Valores Validos.")
except ValueError:
    print(Fore.RESET + 20*"-")
    print(Fore.RED + "ERROR:")
    print(Fore.RED + "fallo al ingresar numeros.")
    exit()

#confirmacion de edad.
año_actual = 2019
edad = año_actual - año_nacimiento 

#confirmacion de ingresos.
if ingresos <= 0:
    print(Fore.RESET + 20*"-")
    print(Fore.RED + f"error usted no puede generar ${ingresos}")

#confirmacion de edad.
if año_nacimiento >= 2019:
    print(Fore.RESET + 20*"-")
    print(Fore.RED + "ERROR:")
    print(Fore.RED + "Usted es muy pequeño o aun no nace!")

elif año_nacimiento < 1500:
    print(Fore.RESET + 20*"-")
    print(Fore.RED + "ERROR:")
    print(Fore.RED + "Usted es una momia!")

#confirmacion de hijos.
if numero_hijos < 0:
    print(Fore.RESET + 20*"-")
    print(Fore.RED + "ERROR:")
    print(Fore.RED + "usted no puede tener hijos negativos.")

#confirmacion de años en banco.
if año_banco < 0:
    print(Fore.RESET + 20*"-")
    print(Fore.RED + "ERROR: ")
    print(Fore.RED + "usted no puede tener años negativos.")

elif edad < año_banco:
    print(Fore.RESET + 20*"-")
    print(Fore.RED + "ERROR: ")
    print(Fore.RED + "usted no puede llevar toda su vida en el banco.")

#confirmacion de credito.
while True:
    if año_banco > 10 and numero_hijos >= 2:
        print(Fore.GREEN + "Credito Aprobado.")
        break

    elif estado_civil == "C" and numero_hijos > 3 and edad > 45 and edad < 45:
        print(Fore.GREEN + "Credito Aprobado.")
        break

    elif ingresos > 2500000 and estado_civil == "S" and vivienda == "U":
        print(Fore.GREEN + "Credito Aprobado.")
        break

    elif ingresos > 3500000 and año_banco > 5:
        print(Fore.GREEN + "Credito Aprobado.")
        break

    elif vivienda == "R" and estado_civil == "C" and numero_hijos >= 2:
        print(Fore.GREEN + "Credito Aprobado.")
        break