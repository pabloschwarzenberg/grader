#Aprobación de créditos

ingreso = eval(input("Escriba sus ingresos en pesos: "))
nac = eval(input("Ingrese año de nacimiento: "))
numero_hijos = eval(input("Ingrese numero de hijos: "))
años_con_banco = eval(input("Ingrese la cantidad de años afiliado al banco: "))
estado_c = input("Ingrese su estado civil ('S': soltero, 'C', casado): ") 
locacion = input("Ingrese lugar de residencia ('U': urbano, 'R': rural): ")

nac_f = 2021 - nac

if (((años_con_banco > 10) and (numero_hijos >= 2)) or (ingreso >= 1) or (nac_F <= 120) or (estado_c == C) or (estado_c == c) or (estado_c == s) or (estado_c == S) or (locacion == U) or (locacion == u) or (locacion == R) or (locacion == r)):
    print("Su credito ha sido: APROBADO")

elif (((estado_c == C or estado_c == c) and (numero_hijos > 3) and (45 <= nac_f <= 55)) or (locacion == U) or (locacion == u) or (locacion == R) or (locacion == r) or (ingreso >= 1) or (años_con_banco >= 1)):
    print("Su credito ha sido: APROBADO")

elif (((ingreso > 2500000) and (estado_c == S or estado_c == s) and (locacion == U or locacion == u)) or (nac_F <= 120) or (numero_hijos >= 0) or (años_con_banco >= 0)):
    print("Su credito ha sido: APROBADO")

elif (((ingreso > 3500000) and (años_con_banco > 5)) or (nac_F <= 120) or (numero_hijos >= 0) or (estado_c == C) or (estado_c == c) or (estado_c == s) or (estado_c == S) or (locacion == U) or (locacion == u) or (locacion == R) or (locacion == r)):
    print("Su credito ha sido: APROBADO")

elif (((locacion == R) or (locacion == r)) and ((estado_c == C) or (estado_c == c)) and (numero_hijos < 2)) or (ingreso >= 1) or (nac_f <= 120) or (años_con_banco >= 0):
    print("Su credito ha sido: APROBADO")

else:
    print("Su credito ha sido: RECHAZADO")