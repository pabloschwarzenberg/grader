#Cálculo del dígito verificador de un rut
rut=input("ingrese numero: ")
largo=len(rut)
multi=2
suma=0
contador=0
while contador!=largo:
    suma+=int(rut[(largo-1)-contador])*multi
    multi+=1
    if multi>7:
        multi=2
    contador+=1
resto=suma%11
resto=11-resto
if resto==11:
    resto=0
elif resto==10:
    resto="k"
print("dv=" + str(resto))
      