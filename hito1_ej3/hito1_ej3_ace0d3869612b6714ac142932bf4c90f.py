# Aprobacion de creditos
ingreso = int(input("Declare su ingreso en pesos: "))
nacimiento = int(input("Declare su ano de nacimiento: "))
hijos = int(input("Declare la cantidad de hijos: "))
banco = int(input("Declare la cantidad de anos en el banco: "))
estado = str(input("Declare su estado civil S [soltero] C [casado]: "))
while not (estado == "C" or estado == "S"):
    estado = str(input("ERROR, Declare su estado civil S [soltero] C [casado]: "))

vive = str(input("Declare si vive en campo o ciudad/ U [urbano] R[rural]: "))
while not (vive =="R" or vive =="U"):
    vive = str(input("ERROR,Declare si vive en campo o ciudad/ U [urbano] R[rural]: "))
if banco >= 10 and hijos >= 2:
    print("APROBADO")
elif estado == "C" and hijos >= 2 and vive =="U":
    print("APROBADO")
elif ingreso > 2500000 and estado =="S" and vive=="U":
    print("APROBADO")
elif ingreso > 3500000 and banco > 5:
    print("APROBADO")
elif vive == "R" and estado =="C" and hijos < 2:
    print("APROBADO")
else:
    print ("RECHAZADO")
