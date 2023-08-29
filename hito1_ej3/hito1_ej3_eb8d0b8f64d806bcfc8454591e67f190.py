Ingresos = float(input("su ingreso en pesos es:"))
Nacimiento = int(input("ingrese su año de nacimiento:"))
Hijos = int(input("ingrese la cantidad de hijos que tiene:"))
Pertenencia = int(input("ingrese la cantidad de años que ha estado en el banco:"))
Estado = str(input("marque si está casado con una C o soltero con una S:"))
Vive = str(input("si vive en el campo ingrese R de rural, o si vive en la ciudad ingrese U de urbano:"))
if (Pertenencia>10 and Hijos>=2):
    print("APROBADO")
else:
    print("RECHAZADO")
if (Estado == "C" and Hijos>3 and 1963<=Nacimiento<=1973):
    print("APROBADO")
else:
    print("RECHAZADO")
if (Ingresos>2500000 and Estado == "S" and Vive == "U"):
    print("APROBADO")
else:
    print("RECHAZADO")
if (Ingresos>3500000 and Pertenencia>5):
    print("APROBADO")
else:
    print("RECHAZADO")
if (Vive == "R" and Estado == "C" and Hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")
