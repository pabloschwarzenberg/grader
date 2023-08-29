#Contestador de celular
def ult_tres(t):
    for i in (t):
    fin=(int(str(i)[-3:]))
def prim_tres(t):
    for i in (t):
    ini=(int(str(i)[3:]))

tel=[]
tel=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
ult_tres(tel)
prim_tres(tel)
if hora>0 and hora<7:
    print("CONTESTAR")
if hora>7 and hora<14 and fin==int(909):
    print("CONTESTAR")
if hora>17 and hora<19 and ini!=int(877):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")