#Contestador de celular
a=int(input("ingrese el numero telefonico:"))
b=int(input("ingrese la hora de llamada:"))
c=str(a)
d=c[5:8]
f=int(d)
g=str(a)
i=g[0:4]
j=int(g)
if(b>=0 and b<=7):
        print("CONTESTAR")
elif (b<=14 and f==909):
        print("CONTESTAR")
elif(b>=17 and b<=19 or j==877):
        print("NO CONTESTAR")
else:
        print("NO CONTESTAR")