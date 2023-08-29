#ENTRADA

hijosvalor = eval(input("numero de hijos:"))
nacimientof = int(input("año de nacimiento:"))
ingresos = eval(input("ingreso:"))
añosantiguedad = eval(input("años de presencia en el banco:"))
civilestado = str(input("estado civil:"))
residencia = str(input("donde vive:"))

#PROCESAMIENTO

años = 2018 - nacimientof

#SALIDA

if años==55: 
    print("RECHAZADO")
    
elif hijosvalor>=2:
    print("APROBADO")
    
if años==45:
    print ("RECHAZADO")
    
elif ingresos>2500000:
    print("APROBADO")
    
elif ingresos>3500000:
    print("RECHAZADO")
    
if añosantiguedad>5:
    print("RECHAZADO")
    
elif residencia==("campo"):
    print("APROBADO")
    
if residencia==("ciudad"):
    print("APROBADO")

if añosantiguedad >= 10:
    print("APROBADO")

if hijosvalor<2:
    print("RECHAZADO")

if civilestado==("casado"):
    print("APROBADO")
    
elif civilestado==("SOLTERO"):
    print("RECHAZADO")
    
