#Contestador de celular
print("Ingrese numero telefonico:")
numero=int(input())
print("Ingrese hora de llamada:")
hora=int(input())
resto=numero%1000
inicio=numero//100000
if(0<=hora<=7):
      print("CONTESTAR")
if(7<hora<14):
    if(resto==909):
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if(14<=hora<17):
    print("NO CONTESTAR")
if(17<=hora<=19):
    if(inicio==877):
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if(19<hora<=23):
    print("NO CONTESTAR")
    
   

