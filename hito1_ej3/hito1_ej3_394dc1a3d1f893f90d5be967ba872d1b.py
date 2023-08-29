#Aprobación de créditos
money = int(input("Por favor escriba cuantos son sus ingresos: "))
N = int(input("Ingrese su año de nacimiento: "))
H = int(input("Ingrese cuantos hijos tiene: "))
A = int(input("Ingrese cuantos años ha estado con nuestro banco: "))
SC = input("Indique su estado civil. Escriba S para indicar que es soltero o C para indicar que es casado: ")
contestado = False
if SC == "S":
    soltero = True
else: soltero = False
UR = input("Indique si vive en campo (escriba R) o ciudad (escriba U): ")
if UR == "R":
    rural = True
else: rural = False
if A > 10 and H >= 2:
    print("APROBADO")
    contestado = True
if not soltero and H > 3 and ((2021 - N) >=45) or ((2021 - N) <= 55) and not contestado:
    print("APROBADO")
    contestado = True
if money > 2500000 and soltero and not rural and not contestado:
    print("APROBADO")
    contestado = True
if money > 3500000 and A > 5and not contestado:
    print ("APROBADO")
    contestado = True
if not soltero and H < 2 and rural and not contestado:
    print("APROBADO")
    contestado = True
if not contestado:
    print("RECHAZADO")