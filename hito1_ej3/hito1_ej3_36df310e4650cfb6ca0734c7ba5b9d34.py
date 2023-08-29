#Aprobación de créditos
ingreso = int(input("ingreso pesos"))
t = int(input("año:"))
nhijos = int(input("numero hijos"))
tbanco = int(input("años en el banco"))
estado = input("S de soltero y C de casado")
campociudad = input("U de urbano y R de rural")
ts = 2022 - t

    
if tbanco >= 10 and nhijos >= 2:
    print("APROBADO")
elif estado == "C" and nhijos>= 3 and años >= 45 and años <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and campociudad == "U":
    print("APROBADO")
elif ingreso > 3500000 and añosbanco > 5:
    print("APROBADO")
elif campociudad == "R" and estado == "C" and nhijos < 2 :
    print("APROBADO")
else:
    print("RECHAZADO")     