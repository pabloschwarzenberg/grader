#Aprobación de créditos
I = int(input("Ingreso en pesos"))
NA = int(input("Año de nacimiento:"))
NHs = int(input("Numero hijos"))
AB = int(input("Años en el banco"))
print("Estado civil")
EC = input("S de soltero y C de casado:")
print("Vive en campo o cuidad")
Lo = input("U de urbano y R de rural")
ts = 2022 - NA


if  AB >= 10 and NHs >= 2:
    print("si APROBADO")
elif EC == "C" and NHs >= 3 and años >= 45 and años <= 55:
    print("si APROBADO")
elif I > 2500000 and EC == "S" and campociudad == "U":
    print("si APROBADO")
elif I > 3500000 and añosbanco > 5:
    print("si APROBADO")
elif Lo == "R" and EC == "C" and NHs < 2 :
    print("si APROBADO")
else:
    print("no RECHAZADO")