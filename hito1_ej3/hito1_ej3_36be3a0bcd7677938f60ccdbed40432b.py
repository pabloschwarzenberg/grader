#Aprobación de créditos
ingreso = int(input("Introduzca sus ingresos (en pesos): "))
añoNacimiento = int(input("Ingrese su año de nacimiento: "))
numeroHijos = int(input("Ingrese cantidad de hijos: "))
añosAfiliado = int(input("Años que lleva afiliado: "))
estadoCivil = input("Su estado civil (S) para soltero, (C) para casado: ")
lugar = input("Indique si vive en campo  (R) o en ciudad (U): ")
edad = 2020 - añoNacimiento
cuarenta = 2020 - 45
cincuenta = 2020 - 55

condicional = (añosAfiliado >= 10 and numeroHijos >= 2) or (estadoCivil == "C" and cuarenta <= añoNacimiento <= cincuenta) or(ingreso > 2500000 and estadoCivil == "S" and lugar == "U") or(ingreso > 3500000 and añosAfiliado > 5) or(lugar == "R" and estadoCivil == "C" and numeroHijos <= 2)

if condicional:
    print("APROBADO")
else:
    print("RECHAZADO")      