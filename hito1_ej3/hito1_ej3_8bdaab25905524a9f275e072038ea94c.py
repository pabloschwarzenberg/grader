#Aprobación de créditos
I = int(input("Ingresos p"))
NA = int(input("Año de nacimiento:"))
NH = int(input("N° de hijos"))
B = int(input("tiempo en el banco"))
print("Estado civil")
EC = input("S de soltero y C de casado:")
print("Vive en campo o cuidad")
L = input("U de urbano y R de rural")
ts = 2022 - NA

if  B >= 10 and NH >= 2:
    print("APROBADO")
elif EC == "C" and NH >= 3 and años >= 45 and años <= 55:
    print("APROBADO")
elif I > 2500000 and EC == "S" and campociudad == "U":
    print("APROBADO")
elif I > 3500000 and añosbanco > 5:
    print("APROBADO")
elif L == "R" and EC == "C" and NH < 2 :
    print("APROBADO")
else:
    print("RECHAZADO")