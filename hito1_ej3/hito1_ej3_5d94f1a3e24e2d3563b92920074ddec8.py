#Aprobación de créditos
def aprovacion_creditos(ingreso,nacimiento,hijos,anos,estado,vivienda):
    
    if anos>10 and hijos>=2:
        return "APROBADO"
    if estado=="C" and hijos>3 and 1962>nacimiento>=1972:
        return "APROBADO"
    if ingreso>2500000 and estado=="S" and vivienda=="U":
        return "APROBADO"
    if ingreso>3500000 and anos>5:
        return "APROBADO"
    if estado=="C" and hijos<2  and vivienda=="R":
        return "APROBADO"
    else:
        return "REPROBADO"
        
        
ingreso=int(input("ingreso:"))
nacimiento=int(input("nacimiento"))
hijos=int(input("hijos:"))
anos=int(input("años:"))
estado=str(input("estado:"))
vivienda=str(input("vivienda:"))
print(aprovacion_creditos(ingreso,nacimiento,hijos,anos,estado,vivienda))
