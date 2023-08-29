#Aprobación de créditos
def aprobacion(ip,an,nh,ab,ec,cc):
    credito = ""
    #ip:Ingreso en pesos, an:Año nacimiento, nh:Número hijos, ab:Años en el banco, ec:Estado civil, cc:Campo o ciudad
    if ab > 10 and nh >= 2:
        credito = "APROBADO"
    elif ec == "C" and nh > 3 and 45 <=(2023-an) <= 55:
        credito = "APROBADO"
    elif ip > 25000000 and ec == "S" and cc == "U":
        credito = "APROBADO"  
    elif ip > 35000000 and ab > 5:
        credito = "APROBADO"
    elif cc == "R" and ec == "C" and nh < 2:
        credito = "APROBADO"  
    else:
        credito = "RECHAZADO"
    print(f"Su crédito fue {credito}")

ingresos = int(input("Ingrese sus ingresos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos que tiene: "))
aniobanco = int(input("Ingrese sus años en el banco: "))
estado = input("Ingrese su estado civil (S:Soltero, C:Casado): ")
lugar = input("Indique donde vive(U:Ciudad/Urbano, R:Campo/Rural): ")
aprobacion(ingresos,nacimiento,hijos,aniobanco,estado,lugar)
