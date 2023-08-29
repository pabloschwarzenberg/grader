a=int(input("ingrese numero telefonico:"))
b=int(input("ingrese hora de llamada"))
contestar=True
no_contestar=False
if a%1000==909 and b<=14 or b<=19:
 print("contestar")
 if 0>=b>=7:
     print(True)
if 17<=b<=19 and a//1000000!=877:
   print("no contestar")
if b>19:
   print("no contestar")
