#Datos
ingresos = int(input("Ingrese la Cantidad de Ingresos en pesos "))
nacimiento = int(input("Ingrese su edad "))
N_hijos = int(input("¿Cuantos hijos tiene? "))
A_banco = int(input("¿Cuantos años lleva en con el banco? "))
estado_civil = str(input("EstadoCivil Soltero (S) o Casado(C) "))
vive = str(input("Donde vive/ Urbano (U) o Rural (R) "))
A = str("APROBADO")
edad = (2021 - nacimiento)
#Requisitos
#1
if A_banco >= 10 and N_hijos >= 2:
    print(A)
    #2
else:
    if estado_civil == "C" and (edad >= 45 and edad <= 55):
        print(A)
#3
    else:
        if ingresos >= 250000 and (estado_civil == "S" and vive == "U"):
            print(A)
            #4
        else:
            if ingresos >= 350000 and A_banco >= 5:
                print(A)
#5
            else:
                if vive == str("R") and (estado_civil == "C" and N_hijos <= 2):
                    print(A)
                else:
                    print("RECHAZADO")