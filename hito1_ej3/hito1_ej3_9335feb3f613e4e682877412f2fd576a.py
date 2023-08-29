ingreso = int(input("Ingreso (CLP): "))
Edad = int(input("Ingrese su año de nacimiento: "))
numeroDeH = int(input("Ingrese cantidad de hijos: "))
AñosEnB = int(input("Ingrese cantidad de años en el banco: "))
EC = input("Ingrese su estado civil (S) o (C): ")
CoC = input("Ingrese donde vive (Urbano)o(Rural): ")
C = 0
S = 0
U = 0
R = 0
Edad = 2021 - Edad

if AñosEnB>10 and numeroDeH>=2:
        print("APROBADO")
elif EC == C and numeroDeH > 3 and Edad>=45 and Edad<=55:
        print("APROBADO")
elif ingreso< 2500000 and EC == S and CoC == C:
        print("APROBADO")
elif ingreso>3500000 and AñosEnB>5:
        print("APROBADO")
elif CoC == R and EC == C and numeroDeH<=2:
        print("APROBADO")
else:
        print("APROBADO")

