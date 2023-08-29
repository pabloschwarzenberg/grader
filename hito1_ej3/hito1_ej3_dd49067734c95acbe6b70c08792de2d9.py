ingreso= int(input("Digite su ingreso mensual en pesos chilenos:"))
nacimiento= int(input("Ingrese su año de nacimiento:"))
ndehijos= int(input("Ingrese cantidad de hijos:"))
apb= int(input("Ingrese la cantidad de años asociado al banco:"))
estadoC= input("ingrese su estado civil, con S para soltero y C para casado:")
lugarV= input("Ingrese si vive en un espacio rural o urbano, con R para rural y U para urbano:")
edad=(2021-nacimiento)
if apb>10 and ndehijos>=2:
    print("APROBADO")
elif estadoC=="C" and ndehijos>3 and edad<55 and edad >45:
    print("APROBADO")
elif ingreso>2500000 and estadoC== "S" and lugarV== "U":
    print("APROBADO")
elif ingreso>3500000 and apb>5:
    print("APROBADO")
elif lugarV=="R" and estadoC=="C" and ndehijos<2:
    print("APROBADO")