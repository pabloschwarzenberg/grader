#Aprobación de créditos
ingreso = int(input("Digame de cuanto es su ingreso:",))
años = int(input("Digame cual es su año de nacimiento:",))
hijos = int(input("¿Cuántos hijos tiene?:",))
años_banco = int(input("¿Hace cuántos años pertenece al banco?:",))
estado = str(input("Ingrese su estado civil. 's' para soltero , 'c' para casado:",)).lower()
zona = str(input("Indique si vive en zona rural o urbana, 'r' o 'u':",)).lower()

años = (2020-años)
#REGLAS

if años_banco>10 and hijos>=2:
    print("\nAPROBADO")
elif estado == "c" and hijos>3 and 45 <años<55:
    print("\nAPROBADO")
elif ingreso > 2500000 and estado == "s" and zona == "u":
    print("\nAPROBADO")
elif ingreso > 3500000 and años_banco > 5:
    print("\nAPROBADO")
elif zona == "r" and estado == "c" and hijos < 2:
    print("\nAPROBADO")
else:
    print("\nRECHAZADO")