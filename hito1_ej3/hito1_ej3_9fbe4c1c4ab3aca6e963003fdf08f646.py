#entrada
from os import system
system("cls")


income = float(input("Introduzca su ingreso mensual: "))
print("Sus ingresos declarados son ", "$" + str(income) + ".")

birth_year = int(input("Introduzca su año de nacimiento: "))
print("Su año de nacimiento ingresado es " + str(birth_year) + ".")

children_quantity = int(input("¿Cuántos hijos tiene?: "))
print("Ha declarado que tiene", children_quantity, "hijos.")

client_years = int(input("¿Por cuántos años ha sido cliente del banco?: "))
print("Ha declarado un total de", client_years, "como cliente.")

marital_status = str(input("¿Cuál es su estado civil? Ingrese 'S' si es soltero, o 'C' si es casado. "))
print("Su estado marital es", marital_status + '.')

home_sector = str(input("¿Vive en una zona urbana o rural? Ingrese 'U' si la zona es urbana, o 'R' para zona rural. "))
print("Ha declarado su zona de residencia como", home_sector + '.')

#proceso
client_age = 2022 - birth_year

isMarried = False
if marital_status == 'C' or marital_status == 'c':
    isMarried = True

isUrban = False
if home_sector == 'U' or home_sector == 'u':
    isUrban = True

if client_years > 10 and children_quantity >= 2:
    print("APROBADO")
elif isMarried == True and children_quantity > 3 and client_age >= 45 and client_age <= 55:
    print("APROBADO")
elif income > 2500000 and isMarried == False and isUrban == True:
    print("APROBADO")
elif income > 3500000 and client_years > 5:
    print("APROBADO")
elif isUrban == False and isMarried == True and children_quantity < 2:
    print("APROBADO")

else:
    print("RECHAZADO")