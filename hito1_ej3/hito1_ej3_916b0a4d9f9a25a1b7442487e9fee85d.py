print("Aprobación de Créditos")
ingreso=int(input("Ingresos en pesos:"))
nacimiento=int(input("Año de nacimiento:"))
hijos=int(input("Número de hijos:"))
añosCliente=int(input("Años de pertenencia al banco:"))
estadoCivil=str(input("Estado civil, S = soltero; C = casado:"))
zonaVivienda=str(input("Residencia, U = urbano; R = rural:"))
if añosCliente>10 and hijos>=2:
    print("APROBADO")
elif estadoCivil=="C" and hijos>3 and nacimiento==1973 or nacimiento==1974 or nacimiento==1975 or nacimiento==1976:
    print("APROBADO")
elif ingreso>2500000 and estadoCivil=="S" and zonaVivienda=="U":
    print("APROBADO")
elif ingreso>3500000 and añosCliente>5:
    print("APROBADO")
elif zonaVivienda=="R" and estadoCivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")