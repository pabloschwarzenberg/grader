#El banco usará las siguientes reglas para decidir la aprobación del crédito, con una de ellas que se cumpla, se aprueba el crédito:
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos. x
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
x = 2020
I = int(input("Escriba su ingreso mensual: "))
N = int(input("Ingrese fecha de nacimiento: "))
H = int(input("Cuantos hijos tiene: "))
A = int(input("Cuantos años lleva usted afiliado al banco"))
E = input("ingrese su estado civil, considere, s es Soltero y c es Casado: ")
L = input("Usted vive en Campo o Ciudad , considere U es Urbano y R Rural: ")
e = (2020 - N )
C = ("Cliente")
S = ("Soltero")
c = ("Casado")
U = ("Urbano")
R = ("Rural")
cc = c
s = S
ur = U
ru = R
if  int(A) >= 10:
    if int(H) >= 2:
        print("CREDITO APROBADO,FELICIDADES")
else:
    print("SU CREDITO HA SIDO RECHAZADO")
    
if cc == c:
      if int(H) >= 3:
        if (45 <= int(e) <= 55):
            print("FELICIDADES, SU CREDITO HA SIDO APROBADO")
else:
    print("SU CREDITO HA SIDO RECHAZADO")

if I >= 2500000:
    if s == S:
        if ur == U:
            print("FELICIDADES, SU CREDITO HA SIDO APROBADO")
else:
    print("SU CREDITO HA SIDO RECHAZADO")
    
if I >= 3500000:
    if A >= 5:
        print("FELICIDADES, SU CREDITO HA SIDO APROBADO")
else:
    print("SU CREDITO HA SIDO RECHAZADO")
    
if ru == R:
    if cc == c:
        if int(H) < 2:
            print("FELICIDADES, SU CREDITO HA SIDO APROBADO") 
else:
    print("SU CREDITO HA SIDO RECHAZADO")