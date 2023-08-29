ingreso= eval(input("Escriba sus ingresos(En pesos): "))
nacimiento=eval(input("ingrese su año de nacimiento: "))
hijos=eval(input("¿Cuántos hijos tiene?: "))
tiempo=eval(input("¿Cuántos años ha pertenecido a este banco?"))
estado_civil=str(input("Estado civil(S: Soltero,C: Casado): "))
espacio=str(input("¿En que área vive?(U: Urbano,R: Rural): "))
edad=2020-nacimiento
if tiempo>10 and hijos>=2:
    print("APROBADO")
elif estado_civil=="C" and hijos>3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingreso>2500000 and estado_civil=="S" and espacio==U:
    print("APROBADO")
elif ingreso>3500000 and tiempo>5:
    print("APROBADO")
elif espacio=="R" and estado_civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
