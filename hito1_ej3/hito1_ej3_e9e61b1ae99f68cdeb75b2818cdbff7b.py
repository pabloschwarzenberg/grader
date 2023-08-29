#Aprobación de créditos
ingreso= int(input("Sus ingresos: "))
nacimiento= int(input("Año de nacimiento: "))
hijos= int(input("Numero de hijos: "))
pbanco= int(input("Años en el banco: "))
civil= input("Esta soltero(a) o Casado(a)|Responda S si es soltero, o C si esta casado: ")
residencia= input("Donde reside|Si es ciudad/urbano U, o si es de campo/rural R: ")

if pbanco > 10 and hijos >=2:
    print("APROBADO")

elif civil==("C" or "C") and hijos > 3 and nacimiento >= 1966 or nacimiento<= 1956:
    print("APROBADO")
 
elif ingreso > 2500000 and civil==("S" or "S") and residencia==("U" or "U"):
    print("APROBADO") 

elif ingreso > 3500000 and pbanco > 5:
    print("APROBADO")

elif residencia==("R" or "R") and civil==("C" or "C") and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")      