#Aprobación de créditos
s = "soltero"
c = "casado"
u = "urbano"
r = "rural"
ingreso = int(input("inserte su ingreso en pesos: "))
ADN = int(input("ingrese su edad: "))
NDH = int(input("ingrese el numero de hijos que tiene: "))
ADP = int(input("ingrese sus años de pertenencia al banco: "))
EC = input("Ingrese su estado civil:  ")
DH = input("Ingrese si vive en campo o ciudad, donde U es urbano y R rural: ")
if ADP>10 and NDH>=2:
    print("APROBADO")
elif EC == c and NDH>3 and ADN>=45 and ADN<=55:
        print("APROBADO")

elif ingreso>2500000 and EC == s and DH == u:
        print("APROBADO")

elif ingreso>35000000 and ADP>5:
        print("APROBADO")

elif DH == r and EC == c and NDH<2:
        print("APROBADO")
else:
        print("APROBADO")      