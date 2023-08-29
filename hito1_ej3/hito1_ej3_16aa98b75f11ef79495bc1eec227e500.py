#aprobacion creditos
#datos a entregar al banco

ingreso = input("Ingreso (en pesos) : ")
añonac = input("Año de nacimiennto : ")
numhijos = input("Número de hijos : ")
añospert = input("Años de pertenencia al banco : ")
estdcivil = input("Estado civil ('S': soltero, 'C', casado) :")
dndvive = input("Si vive en campo o cuidad ('U': urbano, 'R': rural) : " )
numhijos= int(numhijos)

sw = 0

if añospert > "10" and numhijos > 1:
    sw = "1"
    
if estdcivil == "C" and numhijos > 3 and añonac >= "45" and añonac <= "55":
    sw = "1"


if ingreso > "2.500.000" and estdcivil == "S" and dndvive == "U":
    sw = "1"

if ingreso > "3.500.000" and añospert > "5" :
    sw = "1"

    
if dndvive == "R" and estdcivil == "C" and numhijos < 2 :
    sw = "1"

if sw > "0":
    print("APROBADO")
else:
    
    print("RECHAZADO")
      