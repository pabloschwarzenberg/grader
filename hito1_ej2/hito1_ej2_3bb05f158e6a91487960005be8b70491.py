#Contestador de celular
a= int(input("Ingrese numero telefonico: "))
b= int(input("Ingrese hora de la llamada: "))
c= round(((a/1000)-(a//1000))*1000,3)
d= (a//100000)

if (b>=0)and (b<=6):
   print("Resultado: CONTESTAR ")

if (b>=7)and (b<=13) and (c==909):
    print("Resultado: CONTESTAR ")
if(b>=7)and (b<=13) and (c!=909):
   print("Resultado: NO CONTESTAR ")
    
if (b>=14) and (b<=16):
    print("Resultado: NO CONTESTAR ")
   
if (b>=17)and (b<=18) and (d!=877):
    print("Resultado: CONTESTAR ")
if (b>=17)and (b<=18) and (d==877):
    print("Resultado: NO CONTESTAR ")

if (b>=19)and (b<=23):
    print("Resultado: NO CONTESTAR ")     