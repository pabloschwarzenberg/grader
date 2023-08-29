print("Bienvenido al sistema de Creditos")
ingreso = int(input("Digite el monto de ingreso recibido por usted: "))
yearNacim = int(input("Ingrese su año de nacimiento: "))
numHijos = int(input("Ingrese cantidad de hijos (de no tener ingrese 0): "))
yearInBanco = int(input("Ingrese cuantos años lleva usted en el banco: "))
estadoCivil = input("Su estado civil (Soltero = 'S' Casado = 'C')")
ubicacion = input("De donde proviene (Urbano = 'U' Rural = 'R')")
edad = 2020 - yearNacim
if(yearInBanco > 10 and numHijos >= 2):
    print("APROBADO")
elif (estadoCivil == "C" or estadoCivil == "c") and (numHijos >= 3) and (edad >= 45 and edad <= 55):
    print("APROBADO")
elif (ingreso > 2500000 and (estadoCivil == "S" or estadoCivil == "s") and (ubicacion == "u" or ubicacion == "U")):
    print("APROBADO")
elif (ingreso > 3500000 and yearInBanco > 5):
    print("APROBADO")
elif (ubicacion == "R" or ubicacion == "r") and (estadoCivil == "c" or estadoCivil == "C") and (numHijos ==  0 or numHijos == 1):
    print("APROBADO")
else:
    print("RECHAZADO")