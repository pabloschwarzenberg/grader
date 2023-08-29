#Aprobación de créditos
ingreso = eval(input("Cual es su ingreso: "))
año_nacimiento = eval(input("Cual es su año de nacimiento: "))
num_hijos = eval(input("Cuntos hijos tiene: "))
años_banco = eval(input("Cuantos años lleva en el banco: "))
estado = input("Estado civil (S:soltero / C: casado): ")
vive =  input("En donde vive (U: urbano / R: rural): ")
import datetime
if (años_banco > 10 and num_hijos >= 2) or (estado =="C" and
     num_hijos > 3 and
     (datetime.datetime.today().year)-año_nacimiento >= 45 and
     (datetime.datetime.today().year)-año_nacimiento <= 55) or (ingreso > 2500000 and estado =="S" and vive=="U") or (ingreso > 3500000 and años_banco > 5) or (vive == "R" and estado == "C" and num_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")      