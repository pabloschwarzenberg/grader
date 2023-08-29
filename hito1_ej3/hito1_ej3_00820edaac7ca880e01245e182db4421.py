#Aprobación de créditos
Ingreso = input("Su ingreso en pesos: ")
año_n = input("Su edad: ")
n_hijos = input("Numero de hijos: ")
años_b = input("años de pertenecia al banco: ")
e_civil = input("Estado civil, si es soltero (0) o casado (1):", )
domicilio = input("domicilio, rural (0) o urbano (1):", )

soltero = 0
casado = 1

if (e_civil) < str(1) and (e_civil) > str(-1):
    e_civil = soltero 
else:
    e_civil > str(0) and e_civil <str(2)
    e_civil = casado

rural = 0
urbano = 1
if domicilio < str(1) and domicilio > str(-1):
    domicilio = rural
else:
    domicilio < str(2) and domicilio > str(0)
    domicilio = urbano


if años_b > str(10) and n_hijos < str(1):
    print("APROBADO")
elif int(e_civil) > int(0) and int(n_hijos) > int(3) and str(año_n) > str(1964) or str(año_n) < str(1976):
    print("APROBADO")
elif int(e_civil) > int(0) and int(n_hijos) > int(3) and str(año_n) > str(1964) or str(año_n) < str(1976):
    print("APROBADO")
elif ingreso > str(250000) and e_civil < str(1) and domicilio > str(0):
    print("APROBADO")
elif ingreso > str(350000) and años_b > str(5):
    print("APROBADO")
elif domicilio < str(1) and n_hijos < str(2):
    print("APROBADO")      