n = int(input("Ingrese un numero telefonico: "))
h = int(input("Ingrese hora de llamada: "))
fin_num=n%1000
t= n%100000
f=n-(t)
ini_num=f/100000
if(h>=0 and h<=7):
    print("CONTESTAR")
if(h<14 and fin_num==909):
    print("CONTESTAR")
if(h>=17 and h<=19 and ini_num!=877):
    print("CONTESTAR")
if(h>19):
    print("NO CONTESTAR")
if(h>=17 and h<=19 and ini_num==877):
    print("NO CONTESTAR")

 