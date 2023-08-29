#Aprobación de créditos
#ingresar variables
i = int(input("Ingrese sus ingresos: "))
n = int(input(" Ingrese su año de nacimiento: "))
h = int(input("Ingrese su numero de hijos que tiene: "))
a = int(input("Ingrese los años que lleva con nosotros: "))
e = input("Ingrese su estaco civil con una C si esta casado o S si esta soltero: ")
uor = input("Ingrese si vive en ciudad con U o Campo con R: ")
#Resultados
if (i >= 2500000 and e == "S" and uor == "U"):
    print("APROBADO")
elif(i >= 3500000 and a >=5):
    print("APROBADO")
elif(e == "C" and h > 3 and n >= 1966  and n <= 1976 ):
    print("APROBADO")
elif(a > 10 and h >= 2):
    print("APROBADO")
elif(uor == "R" and e == "C" and h < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
#Fin
     