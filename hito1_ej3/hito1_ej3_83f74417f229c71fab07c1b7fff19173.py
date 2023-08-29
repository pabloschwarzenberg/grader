desicion="RECHAZADO"

print("***APROBACIÓN DE CRÉDITOS***")
ingreso=int(input("Ingresos(pesos): "))
print("Ingresos correctamente ingresados!")
nacimiento=int(input("Año de nacimiento. Por ejemplo 1998: "))
print("Nacimiento correctamente ingresados!")
hijos=int(input("Número de hijos: "))
print("Cantidad de hijos correctamente ingresados!")
anosPertenencia=input("Años de pertenencia al banco: ")
print("Años de pertenencia en el banco correctamente ingresados!")

estadoCivil="N"
salida=True
while salida:
  estadoCivil=input("Estado civil (S)=soltero, (C)=casado: ")
  if(estadoCivil=="S" or estadoCivil=="C"):
    print("Estado Civil correctamente ingresados!")
    salida=False
  else:
    print("Se ingresó una letra inválida, vuelva a ingresar por favor")
salida=True
while salida:
  campoCiudad=str(input("Vive en campo o ciudad (U)=urbano, (R)=rural: "))
  if(campoCiudad=="U" or campoCiudad=="R"):
    print("Lugar donde vive correctamente ingresados!")
    salida=False
  else:
    print("Se ingresó una letra inválida, vuelva a ingresar por favor")
    
años=2020-nacimiento
if(int(anosPertenencia)>=10 and hijos>=2):
  desicion="APROBADO"
elif(estadoCivil=="C" and hijos>=3 and años>=45 and años<=55):
  desicion="APROBADO"
elif(ingreso>2500000 and estadoCivil=="S" and campoCiudad=="U"):
  desicion="APROBADO"
elif(ingreso>3500000 and añosPertenencia>5):
  desicion="APROBADO"
elif(campoCiudad=="R" and estadoCivil=="C" and hijos<2):
  desicion="APROBADO"

print("Con los siguientes datos obtenidos usted está: ",desicion)