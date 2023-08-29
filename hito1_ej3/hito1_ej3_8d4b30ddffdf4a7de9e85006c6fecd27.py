#Aprobación de créditos
ing = int(input())
nac = int(input())
hijos = int(input())
banco = int(input())
est = str(input())
cid = str(input())
if banco > 10 and hijos >= 2:
    print ("APROBADO")
if est == "C" and hijos >=3 and nac in range (1962,1973):
    print ("APROBADO")
if ing > 2500000 and est == "S" and cid == "U":
    print ("APROBADO")
if ing > 3500000 and banco > 5:
    print ("APROBADO")
if cid == "R" and est == "C" and hijos < 2:
    print ("APROBADO")
else: 
    print ("REPROBADO")

