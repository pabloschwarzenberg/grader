# Entrada
ingreso = int(input("Cuales son sus ingresos en el banco?: "))
nacimiento = int(input("En que año nació?: "))
hijos = int(input("Cuantos hijos tiene?: "))
aBanco = int(input("Cuantos años tiene con el banco?: "))
print("Indique su estado civil con una C(casado) o S(soltero) ")
estadoCivil = input("Cual es su estado civil?: ")
print("Indique donde vive. Si es en el campo indique con R, si es en ciudad con una U")
vivir = input("En que sector vive?: ")
edad = 2020 - nacimiento
edad = int(edad)

# Aprobacion de creditos
if (aBanco>10 and hijos>=2) or (estadoCivil == "C" and hijos>3 and 45<=edad<=55)\
   or (ingreso>2500000 and estadoCivil == "S" and vivir == "U") or \
   (ingreso>3500000 and aBanco>5) or (vivir == "R" and estadoCivil == "C" and hijos<2):
    print("APROBADO")

else:
    print("RECHAZADO")
      