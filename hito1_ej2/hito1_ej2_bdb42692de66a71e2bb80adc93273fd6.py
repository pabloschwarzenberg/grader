#contestador 
numero=str(input("ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
if(hora in range(0,7)):
  print("CONTESTAR")
if (hora==8 or hora==9 or hora==10 or hora==11 or hora==12 or hora==13 and eval(numero[5])==9 and eval(numero[6])== 0 and eval(numero[7])==9):
  print("CONTESTAR")
if(hora==14 or hora==15 or hora==16):
  print("NO CONTESTAR")
if(hora==17 or hora==18 or hora==19):
  print("CONTESTAR")
if(hora==17 or hora==18 or hora==19 and eval(numero[5])==8 and eval(numero[6])==7 and eval(numero[7])==7):
  print("NO CONTESTAR")
if(hora>19):
  print("NO CONTESTAR")