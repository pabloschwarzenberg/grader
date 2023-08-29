#Aprobación de créditos
i = int( input( "¿Cuánto dinero es su ingreso? "))
an = int( input( "¿En qué año nació? "))
nh = int( input( "¿Cuántos hijos tiene? "))
ap = int( input( "¿Hace cuántos años que pertenece a nuestro banco? "))
ec = str( input( "¿Es usted soltero(a) o casado(a)? "))
cc = str( input( "¿Vive en el campo o en la ciudad? "))

a = str("APROBADO")
r = str("RECHAZADO")

if ( ap > 10 and nh >= 2):
    print(a)
elif ( ec == "C" and nh > 3 and 45 <= 2017 - an <= 55):
    print(a)
elif ( i > 2500000 and ec == "S" and cc == "U"):
    print(a)
elif ( i > 3500000 and ap > 5 ):
    print(a)
elif ( cc == "R" and ec == "C" and nh < 2):
    print(a)
else: print(r)