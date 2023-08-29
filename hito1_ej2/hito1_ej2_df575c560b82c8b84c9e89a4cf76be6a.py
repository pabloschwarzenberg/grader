#Contestador de celular
print("Los números telefónico son de 8 dígitos y la hora es con formato de 24 horas, por ejemplo: 16.15 significa que son las 4 de la tarde con 15 minutos")
a=int(input("Ingrese número telefónico:"))
b=float(input("Ingrese hora de llamada:"))
c=str(a)
d=c[-3:]
e=int(d)
f=c[:3]
g=int(f)
if (b<=7):
    print("Contestar")
elif (e==909) and (7<b<14):
    print("Contestar")
elif (e!=909) and (7<b<14):
    print("No contestar")
elif (14<b<17):
    print("No contestar")
elif (g!=877) and (17<b<19):
    print("Contestar")
elif (g==877) and (17<b<19):
    print("No contestar")
elif (b>19):
    print("No contestar")