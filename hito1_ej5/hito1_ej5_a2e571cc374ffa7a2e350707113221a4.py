# Cálculo del dígito verificador de un rut
r = input("ingrese rut")

R = int(r[0]) #6
A = int(r[1]) #0
B = int(r[2]) #1
C = int(r[3]) #6
D = int(r[4]) #7
E = int(r[5]) #4
F = int(r[6]) #0
if int(r)>=10000000:
    G = int(r[7])
    K = G * 2 + F * 3 + E * 4 + D * 5 + C * 6 + B * 7 + A * 2 + R * 3
    digitb = K % 11
    digitoverificador = 11 - digitb
    if digitoverificador == 10:
        print("dv=k")
    else:
        print("dv=", digitoverificador)
else:
    K= F * 2 + E * 3 + D * 4 + C * 5 + B * 6 + A * 7 + R * 2
    digitb = K % 11
    digitoverificador = 11 - digitb
    if digitoverificador == 10:
        print("dv=k")
    elif digitoverificador >10:
        print("dv = 0")
    elif digitoverificador <10:
        print("dv=", digitoverificador)