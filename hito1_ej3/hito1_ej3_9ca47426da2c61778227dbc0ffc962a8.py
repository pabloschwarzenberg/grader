#Aprobación de créditos
ingreso=eval(input("Ingrese su ingreso en pesos: "))

año=int(input("Ingrese su año de nacimiento: "))

edad= 2020- año

NH=int(input("Ingrese su numero de hijos: "))

AB=float(input("Ingrese cuantos años pertenece al banco: "))

print("Estado civil: ")
print("Las opciones deben ir en minusculas")
print("Ingrese C si es casado/a")
print("Ingrse S si es soltero/a")
EC=(input("Ingrese su estado civil: "))

print("Lugar donde vive: ")
print("Las opciones deben ir en minusculas")
print("Ingrese U si vive en la ciudad")
print("Ingrese R si vive en el campo")
LV=(input("Ingrese el lugar en el que vive: "))

if (AB>10) and (NH>2):
    print("APROBADO")

elif(EC == "c") and (NH>3) and (45<edad<55):
    print("APROBADO")

elif(ingreso>2500000) and (EC == "s") and (LV == "u"):
    print("APROBADO")

elif(ingreso>3500000) and (AB>5):
    print("APROBADO")

elif(LV=="r") and (EC == "c") and (NH<2):
    print("APROBADO")

else:
    print("NO APROBADO")