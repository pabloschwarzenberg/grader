#Aprobación de créditos
ing= int(input("Sus ingresos: "))
nacido= int(input("Año de nacimiento: "))
nhijos= int(input("Numero de hijos: "))
pbanco= int(input("Años en el banco: "))
tcivil= input("Esta soltero(a) o Casado(a)|Responda S si es soltero, o C si esta casado: ")
residencia= input("Donde reside|Si es ciudad/urbano U, o si es de campo/rural R: ")

#Años de antiguedad
if pbanco > 10 and nhijos >=2:
    print("APROBADO")

#Si es casado y 3o+ hijos, y tiene entre 45 y 55
elif tcivil==("C" or "C") and nhijos > 3 and nacido >= 1966 or nacido <= 1956:
    print("APROBADO")
 
#Si el gana+ de 2500000, es soltero y vive en ciudad
elif ing > 2500000 and tcivil==("S" or "S") and residencia==("U" or "U"):
    print("APROBADO") 

#Si el cliente supera + 3500000 y pertenece al banco +5 años
elif ing > 3500000 and pbanco > 5:
    print("APROBADO")

#Si el cliente es del campo, es casado y tiene - de 2 hijos.
elif residencia==("R" or "R") and tcivil==("C" or "C") and nhijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")      