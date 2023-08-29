#Contestador de celular
numero=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
ptres=(numero//100000)
utres=numero % 1000
if(0<=hora<=7):
    print("Resultado: CONTESTAR")
if(7<hora<=14)and(utres!=909):
    print("Resultado: NO CONTESTAR")
if(hora<=14)and(utres==909):
    print("Resultado: CONTESTAR")
if(14<hora<17):
    print("Resultado: NO CONTESTAR")
if(17<=hora<=19)and (ptres!=877):
    print("Resultado: CONTESTAR")
if(17<=hora<=19 and ptres==877):
    print("Resultado: NO CONTESTAR")
if(hora>19):
    print("Resultado: NO CONTESTAR")