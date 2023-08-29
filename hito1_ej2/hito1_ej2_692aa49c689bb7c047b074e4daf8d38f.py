a = int(input("ingresa numero telefonico:"))
h = int(input("ingresa hora de la llamada:"))

if (0<h<7):
           print("CONTESTAR")


if (7<h<14)and (a%1000)//1 == 909:
           print("CONTESTAR")
             
if (7<h<14)and (a%1000)//1 != 909:
   print("no contestar")

if(14<h<17):
    print("no contestar")

if(17<h<19)and(a%100000000)//100000 == 877:
    print("no contestar")
if(17<h<19)and(a%100000000)//100000 != 877:
    print("contestar")

if (19<h<24):
    print("No contestar")

      