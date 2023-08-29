#Contestador de celular
numero_telefonico=input("Ingrese numero telefonico: ")
hora_llamada=input("Ingrese hora de la llamada: ")
n=909
m=87700000

if 0<=int(hora_llamada)<=7:
    print("CONTESTAR")

if 7<int(hora_llamada)<14 and not((int(numero_telefonico)-n)%1000==0):
    print("NO CONTESTAR")

if 7<int(hora_llamada)<14 and ((int(numero_telefonico)-n)%1000==0):
    print("CONTESTAR")

if 14<=int(hora_llamada)<17:
    print("NO CONTESTAR")

if 17<=int(hora_llamada)<19 and not((int(numero_telefonico)-m)<=99999):
    print("CONTESTAR")

if 17<=int(hora_llamada)<19 and((int(numero_telefonico)-m)<=99999):
    print("NO CONTESTAR")

if 19<=int(hora_llamada)<24:
    print("NO CONTESTAR")
