#Aprobación de créditos
ingreso_en_pesos = eval(input("ingrese en pesos sus ingresos mensuales :"))
año_de_nacimiento = eval(input("ingrese su años de nacimiento ej:1993: "))
numero_de_hijos= eval(input("ingrese el numero de hijos ej :" ))
años_de_pertenencia_en_el_banco= eval(input("ingrese los años que ha pertenecido al banco: "))
estado_civil= input("ingrese su estado civil ej:S soltero, C casado: ")
donde_vive= input("indique donde vive, U urbano o R rural: ")
C = "C"
S="S"
U="U"
R="R"

edad= 2021-año_de_nacimiento

if    (años_de_pertenencia_en_el_banco > 10) and (numero_de_hijos  >=2):
     print("APROBADO")
elif (estado_civil == C) and (numero_de_hijos >3)and(edad > 45 and edad < 55):
     print("APROBADO")
elif (ingreso_en_pesos > 2500000) and (estado_civil == S) and (donde_vive== U):
     print("APROBADO")
elif (ingreso_en_pesos > 3500000) and (años_de_pertenencia_en_el_banco > 5):
     print("APROBADO")
elif (donde_vive==R) and (estado_civil == C)and (numero_de_hijos < 2):
     print("APROBADO")
     
else:
    print("RECHAZADO")
      