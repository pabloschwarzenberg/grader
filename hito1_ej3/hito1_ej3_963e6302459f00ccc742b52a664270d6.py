#Aprobación de créditos
ingresoMes=int(input("Ingrese su sueldo:"))
anoNacimiento=int(input("Ingrese año de nacimiento:"))
numDeHijos=int(input("Ingrese número de hijos:"))
anosBanco=int(input("Ingrese años de cliente en el Banco:"))
estadoCivil=str(input("Ingrese estado civil (Soltero o Casado [S|C]):")).lower()
lugarVive=str(input("Ingrese domicilio (Urbano o Rural [U|R]):")).lower()
if anosBanco>10 and numDeHijos>=2 or estadoCivil=="c" and numDeHijos>3 and ((anoNacimiento-2020)*-1)>45 and ((anoNacimiento-2020)*-1)<55 or ingresoMes>2500000 and estadoCivil=="s" and lugarVive=="u" or ingresoMes>3500000 and anosBanco>5 or lugarVive=="r" and estadoCivil=="c" and numDeHijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")