#Contestador de celular
t = int(input("ingrese numero telefonico:"))
h = int(input("ingrese hora de llamada:"))
c=str(t)
d=c[5:8]
f=int(d)
g=str(t)
i=g[0:4]
j=int(g)
if(h>=0 and h<=7):
                 print("CONTESTAR")

elif (h<=14 and f==909 ):
                 print("CONTESTAR")

elif(h>=17 and h<=19 or j==877):
                
                 print("NO CONTESTAR")
                 
else:
                 print("NO CONTESTAR")