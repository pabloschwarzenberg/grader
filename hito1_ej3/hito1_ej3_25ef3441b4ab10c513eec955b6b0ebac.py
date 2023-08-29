#Aprobación de créditos
print("POSTULA A UN CRÉDITO DE CONSUMO")
ingreso=int(input("Ingresos mensuales: "))
añoDeNacimiento=int(input("Edad: "))
numeroDeHijos=int(input("Cuantos hijos tiene: "))
añosDePertenencia=int(input("Años de pertenencia al banco: "))
estadoCivil=str(input("Estado civil: S: Soltero, C: Casado "))
campoOCiudad=str(input("Residencia en: Ciudad: U, Campo: R "))
A="APROBADO"
R="RECHAZADO"
if añosDePertenencia>10 and numeroDeHijos>=2:
    print(A)
if estadoCivil=="C" or estadoCivil=="c":
    if numeroDeHijos>3:
        if añoDeNacimiento>=45 and añoDeNacimiento<=55:
            print(A)
if ingreso>2500000:
    if estadoCivil=="S" or estadoCivil=="s":
        if campoOCiudad=="U" or campoOCiudad=="u":
            print(A)
if ingreso>3500000 and añosDePertenencia>5:
    print(A)
if campoOCiudad=="R" or campoOCiudad=="r":
    if estadoCivil=="C" or estadoCivil=="c":
        if numeroDeHijos<2:
            print(A)
print(R)