#Entrada
sueldo = int(input("Ingrese su ingreso en pesos: "))
ano = int(input("ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
anoBanco = int(input("Ingrese la cantidad de años en el banco: "))
civil = str(input("Ingrese una ¨S¨ si esta soltero y una ¨C¨ si esta casado: "))
hogar = str(input("Ingrese ¨U¨ si vive en un lugar urbano y una ¨R¨ si es de una sona rural: "))

#Proceso
if anoBanco >= 10 and hijos >= 2:
    print("APROBADO")
elif civil == "C" and hijos >= 3 and (ano >= 1965 or ano <= 1975):
    print("APROBADO")
elif civil == "S" and hogar == "U" and sueldo >= 2500000:
    print("APROBADO")
elif sueldo >= 3500000 and anoBanco >= 5:
    print("APROBADO")
elif civil == "C" and hogar == "R" and hijos <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
   