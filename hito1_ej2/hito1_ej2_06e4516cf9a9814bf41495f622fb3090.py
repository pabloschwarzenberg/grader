n=int(input("introdusca el numero telefonico: "))
h=int(input("introdusca la hora de la forma 0-23: "))
while(n>99999999):
    print("su numero no tiene 8 cifras")
    n = int(input("introdusca el numero telefonico: "))
while(h>23):
    print("la hora no esta correcta")
    h = int(input("introdusca la hora de la forma 0-23: "))
if(h<=7):
    print("CONTESTAR")
C=str(n)
d=C[5:8]
F=int(d)
if(h<14 or F==909):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
C=str(n)
d=C[0:4]
F=int(d)
if(h==17 or 18 or 19 and F==877):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
if(h>19):
    print("NO CONTESTAR")