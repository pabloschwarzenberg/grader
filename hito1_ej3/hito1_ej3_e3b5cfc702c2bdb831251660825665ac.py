#Aprobación de créditos
print("Ingreses los datos de los pesos")

Ingreso = int(input())

print("Ingreses año de nacimiento")

nacimiento = int(input())

print("Ingreses el numero de hijos")

Numero_hijos = int(input())

print("Ingreses ingrese el año que lepertenece al banco")

pertenencia_banco = int(input())

print("Ingreses el estado civil")

Estado_civil = input().lower()

print("Ingreses Campo o ciudad")

campo_ciudad = input().lower()

Edad   = nacimiento - 2022

if pertenencia_banco > 10  and Numero_hijos >= 2:
    
    print("APROBADO")


#------------------------------------------------

if Estado_civil =='c' and Numero_hijos > 3 and Edad  >= 45 and Edad <= 55:
        
    print("APROBADO")



#-------------------------------------------------



if Ingreso > 2500000 and Estado_civil == 's' and campo_ciudad == 'u':
    
    print("APROBADO")


#-------------------------------------------------

if Ingreso > 3500000 and pertenencia_banco > 5:

    print("APROBADO")



if campo_ciudad == 'r' and Estado_civil == 'c' and Numero_hijos < 2:

    print("APROBADO")
    
else:

    print("RECHAZADO")     