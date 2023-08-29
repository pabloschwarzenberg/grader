#Cálculo del dígito verificador de un rut
rut=input("rut")
largo=len(rut)
cont=0
multi=2
suma=0
while cont!=largo:
    suma+=int(rut[(largo-1)-cont])*multi
    multi+=1
    if multi>7:
        multi=2
    cont+=1
resto=suma%11
resto=11-resto
if resto==10:
    resto="k"
elif resto==11:
    resto=0
print("dv="+str(resto))