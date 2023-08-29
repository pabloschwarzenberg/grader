numero=input("Ingrese número telefónico:")
numero=str(numero)

hora=int(input("Ingrese hora de la llamada:"))

if 0<=hora<=7:
   print("CONTESTAR")   
elif hora<14 and (int(numero[5])==9 and int(numero[6])==0 and int(numero[7])==9):
   print("CONTESTAR")
elif hora<14:
   print("NO CONTESTAR")
if 14<=hora<17:
   print("NO CONTESTAR")   
if 17<=hora<=19 and (int(numero[0])==8 and int(numero[1])==7 and int(numero[2])==7):
   print("NO CONTESTAR")
elif 17<=hora<=19:
   print("CONTESTAR")
elif 19<hora:
   print("NO CONTESTAR")
    

