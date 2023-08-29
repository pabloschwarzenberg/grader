print("aprobacion de credito")
P = int(input("Ingrese sus ingresos en pesos: "))
Anio = int(input("Año de nacimiento: "))  #año
Hijos = int(input("Ingrese numero de hijos: "))
Aniob = int(input("Ingrese los años que ha estado en el banco: "))
Ecivil = input(print(" 'S' si esta soltero, 'C' si esta casado: "))
Camporci = input(print(" 'R' si es rural, 'U' de urbano: "))
C = "C"
S = "S"
R = "R"
U = "U"

if Aniob > 10 and Hijos >= 2:
    print("APROBADO")
elif Ecivil == C and Hijos > 3 and 1965 <= Anio >= 1975:
    print("APROBADO")
elif P > 2500000 and Ecivil == S and Camporci == U:
    print("APROBADO")
elif P > 3500000 and Aniob > 5:
    print("APROBADO")
elif Camporci == R and Ecivil == C and Hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      