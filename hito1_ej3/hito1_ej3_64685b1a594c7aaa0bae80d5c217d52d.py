#Aprobación de créditos
a = int(input("Ingrese un monto:"))
b = int(input("Ingrese el año en que nació:"))
c = int(input("Ingrese su número de hijos:"))
d = int(input("Ingrese los años en los que ha pertenecido al banco:"))
e = str(input("Ingrese su estado civil:"))
f = str(input("Donde vive:"))

Edad = 2021 - b

if d>=10:
    print("Aprobado")
elif d < 10:
    print("Rechazado")
if c>=2:
    print("Aprobado")
elif c<2:
    print("Rechazado")
if e==("casado"):
    print("Aprobado")
elif e==("soltero"):
    print("Rechazado")
if Edad == 45:
    print ("Aprobado")
elif Edad == 55: 
    print("Aprobado")
if a>2500000:
    print("Aprobado")
elif a<2500000:
    print("Rechazado")
          
elif a>3500000:
    print("Aprobado")
elif d>5:
    print("Aprobado")
if f==("campo"):
    print("Aprobado")
elif f == (" "):
    print("Rechazado")
if f==("ciudad"):
    print("Aprobado")
elif f == (" "):
    print("Rechazado")      