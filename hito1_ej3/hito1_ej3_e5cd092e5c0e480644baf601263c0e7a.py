#aprobacion de credito
ingresos = int(input("Ingrese su ingreso en pesos: "))
añodenacimiento = int(input("Ingrese su año de nacimiento: "))
nhijos = int(input("Ingrese la cantidad de hijos que tiene: "))
banco = int(input("Ingrese la cantidades de años que lleva asociado a nuestro banco: "))
ec = input("Ingrese su Estado civil, ponga S si esta soltero o coloque una C si esta casado: ")
vivienda = input("Donde vive actualmente: -coloque U si vive en un espaio Urbano o Coloque R si vive en un espacio Rural: ")

fechaactual = int(2020)
edad = fechaactual - añodenacimiento
if banco >= 10 and nhijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
    
if ec == "C" and nhijos > 3 and 45 <= edad <= 55:
    print("APROBADO")
else:
    print("RECHAZADO")
    
if ingresos >= 2500000 and ec == "S" and vivienda == "U":
    print("APROBADO")
else:
    print("RECHAZADO")
    
if ingresos >= 3500000 and banco > 5:
    print("APROBADO")
else:
    print("RECHAZADO")

if vivienda == "R" and ec == "C" and nhijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO") 