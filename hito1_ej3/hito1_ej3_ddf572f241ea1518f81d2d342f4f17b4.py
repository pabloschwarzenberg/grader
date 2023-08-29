I = int(input("Cantidad de ingresos en CLP:"))
AN = int(input("Ingrese su año de nacimiento:"))
AA = 2021 - AN
NH = int(input("¿Cuántos hijos tiene?:"))
A_con_el_banco = int(input("¿Cuántos años ha sido cliente en nuestro banco?:"))
EC = str(input("Por favor indique su estado civil (Una S si está soltero o una C si está casado):"))
Vivienda = str(input("Si vive en un sector rural marque R o, si es un sector urbano, una U:"))
if NH >= 2 and A_con_el_banco > 10:
    print("APROBADO")
elif EC =="c" and NH > 3 and AA <= 55 and  AA >= 45:
    print("APROBADO")
elif I >= 2500000 and EC == "S" and Vivienda == "U":
    print("APROBADO")
elif Vivienda == "R" and EC == "C" and NH < 2:
    print("APROBADO")
elif I > 3500000 and A_con_el_banco > 5:
    print("APROBADO")
else:
    print("RECHAZADO")
