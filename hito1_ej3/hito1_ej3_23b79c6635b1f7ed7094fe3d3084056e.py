#Aprobación de créditos
print("Ingrese la informacion correspondiente")
ingresos = eval(input("Cuanto es el ingreso: "))
añonac = eval(input("Ingrese el año de nacimiento: "))
nhijos = eval(input("Ingrese la cantidad de hijos: "))
añosbanc = eval(input("Ingrese cuantos años lleva perteneciendo al banco: "))
estadociv = input("Ingrese si usted es Soltero (S) o Casado (C)")
zona = input("Ingrese si usted vive en zona Urbana (U) o Rural(R)")

if añosbanc >= 10 and nhijos >= 2:
    print("APROBADO")
    
if estadociv == "C" and nhijos >= 3 and (2020-añonac >= 45 and 2020-añonac <= 55):
    print("APROBADO")
  
if ingresos >= 2500000 and estadociv == "S" and zona == "U":
    print("APROBADO")
    
if ingresos >=3500000 and añosbanc >= 5:
    print("APROBADO")
    
if zona == "R" and estadociv == "C" and nhijos <= 2:
    print("APROBADO")
    
else:
    print("RECHAZADO")
    