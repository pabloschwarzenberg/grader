#Aprobación de créditos
print("favor ingresar los siguientes datos: ")

ingresos=int(input("indique su ingreso en pesos: "))
añoN=int(input("ingrese su año de nacimiento: "))
Nhijos=int(input("ingrese su numero de hijos: "))
añoB=int(input("ingrese la cantidad de años que lleva en el banco: "))
print("soltero= S, casado= C")
ECivil=str(input("ingrese su estado civil S/C: "))
print("campo=R, ciudad=U")
vive=str(input("ingrese si vive en campo o ciudad: "))


edad= añoN-2020

if añoB>10 and Nhijos >=2:
    print("APROBADO")
elif ECivil== "C" and Nhijos>3 and 45<=edad>=55:
    print("APROBADO")
elif ingresos >2500000 and ECivil =="S" and vive=="U":
    print("APROBADO")
elif ingresos>3500000 and añoB>5:
    print("APROBADO")
elif vive == "R" and Nhijos <2:
    print("APROBADO")
else:
    print("RECHAZADO")      