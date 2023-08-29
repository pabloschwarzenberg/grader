import math
numero=(input("Numero:"))
if len(numero)==4:
   print(numero[0:1],"M","+",numero[1:2],"C","+",numero[2:3],"D","+",numero[3:4],"U")
elif len(numero)==3:
   print(numero[0:1],"C","+",numero[1:2],"D","+",numero[2:3],"U")
elif len(numero)==2:
   print(numero[0:1],"D","+",numero[1:2],"U")