Ingreso = int(input("Ingreso pesos:"))
edad = int(input('Input año de nacimiento: '))
Numeros = int(input('Ingrese numero de hijos: '))
permanencia = int(input('año de permanencia al banco: '))
civil = input("Ingrese estado civil (S) o (C): ")
domicilio = (input("Ingrese si vive campo(R) o ciudad(U): "))

X = edad - 2021
if permanencia >= 10 and Numeros >= 2  or civil == 'C'and Numeros > 3 and X >=45 and X <= 55 or Ingreso > 2500000 and civil == 'S' and domicilio == 'U'or  Ingreso  > 35000000 and permanencia > 5 or domicilio == 'R' and Numeros < 2 and civil == 'C':
    print('APROBADO')
if permanencia <= 10 and Numeros < 2 or civil == 'S' and Numeros < 3 or X <=45 and X >= 55 or  Ingreso < 2500000 or civil == 'C' and domicilio == 'R' or  Ingreso < 3500000 and permanencia < 5 or  domicilio == 'U' or Numeros > 2 and civil =='S':
    print('RECHAZADO')
