#Aprobación de créditos
ingresos = int(input("Ingrese la cantidad de ingresos en pesos"))
nacimiento = int(input("Ingrese su año de nacimiento"))
N_hijos = int(input("¿Cuantos hijos tiene? "))
A_banco = int(input("¿cuanto tiempo lleva como cliente del banco?"))
estado_civil = str(input("EstadoCivil Soltero (S) o Casado(C)"))
vive = str(input("Donde se ubica? Urbano (U) o Rural (R)"))
A = str("APROBADO")
edad = (2021 - nacimiento)
if A_banco >= 10 and N_hijos >= 2:
    print(A)
else:
    if estado_civil == "C" and (edad >= 45 and edad <= 55):
        print(A)
    else:
        if ingresos >= 2500000 and (estado_civil == "S" and vive == "U"):
         print(A)
        else:
            if ingresos >= 3500000 and A_banco >= 5:
             print(A)
            else:
                if vive == str("R") and (estado_civil == "C" and N_hijos <= 2):
                 print(A)
                else:
                    print("RECHAZADO")