#Contestador de celular
 n=str(input("ingrese numero telefonico: "))
h=int(input("Ingrese hora de la llamada: "))

if(h in range(0,7)):
    print("CONTESTAR")
if (h==8 or h==9 or h==10 or h==11 or h==12 or h==13 and eval(n[5])==9 and eval(n[6])== 0 and eval(n[7])==9):
    print("CONTESTAR")
if(h==14 or h==15 or h==16):
    print("NO CONTESTAR")
if(h==17 or h==18 or h==19):
    print("CONTESTAR")
if(h==17 or h==18 or h==19 and eval(n[5])==8 and eval(n[6])==7 and eval(n[7])==7):
    print("NO CONTESTAR")
if(h>19):
    print("NO CONTESTAR")     