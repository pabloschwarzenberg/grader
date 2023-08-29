#Contestador de celular
t=int(input("ingrese numero telefono: "))
h=int(input("ingrese hora de la llamada: "))
t1=t//100000
t2=t%1000
#print(t1)
#print(t2)
if h<=7 or h>=17 and h<=19 and t1!=877 or h>7 and h<14 and t2==909:
    print("CONTESTAR")
else:
    h>19 or h>7 and h<14 and t2!=909
    print("NO CONTESTAR")