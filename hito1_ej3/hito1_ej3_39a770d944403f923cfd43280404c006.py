print("Hola, este es el sistema de postulacion a creditos de consumo.Por favor complete el siguiente formulario para saber si usted puede optar a un credito")
Ingreso=int(input("Ingrese aqui su sueldo: "))
anonacimiento=int(input("Año de nacimiento: "))
edad=int(2021-anonacimiento)
nhijos=int(input("Numero de hijos: "))
anosbanco=int(input("Cantidad de años en este banco: "))
print("IMPORTANTE: S=soltero"
      "C=casado")
estadocivil=str(input("Estado civil:"))
print("IMPORTANTE:U=urbano"
      "R=rural")
ddvive=str(input("Lugar donde vive es urbano o rural:"))
if anosbanco>=10 and nhijos >= 2 or (estadocivil=="S" and nhijos>=3 and edad>=45 and edad<=55) or (Ingreso>=2500000 and estadocivil=="S") and (ddvive =="U" or Ingreso>=3500000 and  anosbanco>=5) or (ddvive=="R" and estadocivil=="C" and nhijos<=2):
    print("APROBADO")
else:
    print("RECHAZADO")
