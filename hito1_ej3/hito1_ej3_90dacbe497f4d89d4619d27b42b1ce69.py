#Aprobación de créditos
ingreso=int(input("Ingrese monto de ingresos: "))
brithyear=int(input("Ingrese año de nacimiento: "))
n_hijos=int(input("¿cuántos hijos tiene?:\n"))
n_perteneciente=int(input("Cuántos años es cliente?\n"))
estado_civil=input("Seleccione su estado civil\n'S' para soltero, 'C' para casado: ")
residencia=input("Seleccione su residencia?\n'U' para urbano, 'R' para rural: ")
years=2022-brithyear
if n_perteneciente > 10 and n_hijos >= 2:
    print("APROBADO")
if estado_civil == 'C' and n_hijos > 3 and years >= 45 and years <= 55:
    print("APROBADO")
if ingreso > 2500000 and estado_civil == 'S' and residencia == 'U':
    print("APROBADO")
if ingreso > 3500000 and n_perteneciente > 5:
    print("APROBADO")
if residencia == 'R' and estado_civil == 'C' and n_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")    
 