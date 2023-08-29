#Aprobación de créditos
P = int(input("pesos"))
AN = int(input("Año de nacimiento:"))
NDH = int(input("Nro de hijos"))
AB = int(input("Años en el banco"))
SC = input("S de soltero y C de casado:")
UR = input("U de urbano y R de rural")
ts = 2022 - AN


if  AB >= 10 and NDH >= 2:
    print("APROBADO")
elif SC == "C" and NDH >= 3 and años >= 45 and años <= 55:
    print("APROBADO")
elif P > 2500000 and SC == "S" and campociudad == "U":
    print("APROBADO")
elif P > 3500000 and añosbanco > 5:
    print("APROBADO")
elif UR == "R" and SC == "C" and NDH < 2 :
    print("APROBADO")
else:
    print("RECHAZADO")      