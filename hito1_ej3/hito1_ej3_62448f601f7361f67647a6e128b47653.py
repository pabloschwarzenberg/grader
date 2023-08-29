#Aprobación de créditos
print("Hola, por favor ingrese sus siguientes datos")
ingreso = float(input("Cantidad de ingreso en pesos chilenos sin puntos: "))
edad = int(input("Año de nacimiento: "))
hijos = int(input("Cantidad de hij@s: "))
años = float(input("Cantidad de años perteneciendo al banco: "))
civil = str(input("Estado civil, indicar C para casado y S para soltero: "))
ubicacion = str(input("Dónde se úbica su vivienda, indicar U para espacio urbano y R para espacio rural: "))

if str(civil[0:1]) != "C" and str(civil[0:1]) != "S":
    print("Su estado civil es inválido, debe ser una C o una S.")
if str(ubicacion) != "U" and str(ubicacion) != "R":
    print("Su ubicación es inválida, debe ser una U o una R.")


if años > 10 and hijos >= 2:
    print("APROBADO")
elif civil == "C" and hijos > 3 and edad >= 1976 and edad <= 1966:
    print("APROBADO")
elif ingreso > 2500000 and civil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and años > 5:
    print("APROBADO")
elif ubicacion == "R" and civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")


                                                                                    
                                                           
