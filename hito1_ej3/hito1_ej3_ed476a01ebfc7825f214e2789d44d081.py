#Aprobación de Créditos

#Entrada

ingresos = int(input("Digite sus ingresos: "))
birth = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese su número de hijos: "))
pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
estadoCivil = input("Ingrese su estado civil: (C/S)")
ubicacion = input("Ingrese si vive en ambiente Urbano o Rural: (U/R)")

if pertenencia>10 and hijos>=2 :
    print("APROBADO")
elif estadoCivil == 'C' or estadoCivil == 'c' and hijos>3 and birth<=1975 :
    print("APROBADO")
elif ingresos>2500000 and estadoCivil == 'S' or estadoCivil == 's' and ubicacion == 'U' :
    print("APROBADO")
elif ingresos>3500000 and pertenencia>5 :
    print("APROBADO")
elif ubicacion == 'R' or ubicacion == 'r' and estadoCivil == 'C' or estadoCivil == 'c' and hijos<2 :
    print("APROBADO")
else :
    print("RECHAZADO")
