#Aprobación de créditos

a = int(input("Ingrese su ingreso en pesos: "))
b = int(input("Ingrese su año de nacimiento: "))
c = int(input("Ingrese numero de hijos: "))
d = int(input("Ingrese su año de pertenencia al banco: "))
e = input("Ingrese S si es soltero y C si es casado: ")
f = input("Ingrese U si vive en ciudad y R si vive en campo: ")

if (d > 10) and (c >= 2):
      print("APROBADO")
      
elif (e == "C") and (c > 3) and (1973 <= b <= 1963):
      print("APROBADO")
      
elif (a > 2500000) and (e == "S") and (f == "U"):
      print("APROBADO")

elif (a > 3500000) and (d > 5):
      print("APROBADO")

elif (f == "R") and (e == "C") and (c < 2):
      print("APROBADO")
      
else: 
      print("REPROBADO")