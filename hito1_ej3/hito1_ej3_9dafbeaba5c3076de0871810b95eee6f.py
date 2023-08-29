#Aprobación de créditos
ingreso=int(input("Escriba su ingreso en pesos chilenos: "))
añoNacimiento=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("¿Cúantos hijos tiene?: "))
añoPertenencia=int(input("¿Desde cuando es nuestro cliente?: "))
estadoCivil=str(input("¿Cúal es su estado civil? S/C: "))
dondeVive=str(input("¿Qué sector corresponde donde vive? U/R:  "))
edad=2020-añoNacimiento
perteneceAlBanco=2020-añoPertenencia


if perteneceAlBanco > 10 and hijos >= 2:
 print("APROBADO")
elif estadoCivil == "C"  and hijos > 3 and edad >= 45 and edad <= 55:
 print("APROBADO")
elif ingreso > 2500000 and estadoCivil == "S" and dondeVive == "U":
 print("APROBADO")
elif ingreso > 3500000 and perteneceAlBanco > 5:
 print("APROBADO")
elif dondeVive == "R" and hijos < 2:
 print("APROBADO")
else:
 print("RECHAZADO")
      