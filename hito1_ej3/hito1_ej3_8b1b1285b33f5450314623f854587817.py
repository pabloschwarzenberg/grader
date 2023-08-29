ingreso=int(input("Ingrese sus ingresos en pesos :"))
ano_nacimiento=int(input("Ingrese su año de nacimiento :"))
num_hijos=int(input("Ingrese la cantidad de hijos :"))
anos_banco=int(input("Ingrese los años que pertenece al banco :"))
estado_civil=str(input("Estado civil :"))
tipo_vivienda=str(input("Tipo de vivienda :"))

estado_credito=0

if anos_banco>10 and num_hijos>=2:
    estado_credito=1
if estado_civil=="C" and num_hijos==3 and ano_nacimiento>=1965 and ano_nacimiento<=1975:
    estado_credito=1
if ingreso>2500000 and estado_civil=="S" and tipo_vivienda=="U":
    estado_credito=1
if ingreso>3500000 and anos_banco>5:
    estado_credito=1
if tipo_vivienda=="R" and estado_civil=="C" and num_hijos<2:
    estado_credito=1

if estado_credito==1:
    print("APROBADO")
if estado_credito==0:
    print("RECHAZADO")