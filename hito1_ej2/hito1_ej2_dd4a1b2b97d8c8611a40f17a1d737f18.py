#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
n=str(numero)
h=13
h=int(input("Ingrese hora de llamada: "))
if 0<=h<=7:
    print("RESULTADO:CONTESTAR")
if 7<h<14 and n[5:8]=="909":
    print("RESULTADO:CONTESTAR")
if 7<h<14 and n[5:8]!="909":
    print("RESULTADO:NO CONTESTAR")
if 14<=h<17:
    print("RESULTADO:NO CONTESTAR")
if 17<=h<=19 and n[0:3]=="877":
    print("RESULTADO:NO CONTESTAR")
if 17<=h<=19 and n[0:3]!="877":
    print("RESULTADO: CONTESTAR")
if 19<h<=23:
    print("RESULTADO:NO CONTESTAR")      