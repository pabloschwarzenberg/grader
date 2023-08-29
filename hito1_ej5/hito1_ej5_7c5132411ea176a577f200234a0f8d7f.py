rut=input()
largo=len(rut)
mul=2
contador=0
suma=0
while contador!=largo:
    suma+=int(rut[(largo-1)-contador])*mul
    mul+=1
    if mul>7:
        mul=2
    contador+=1
resto=suma%11
resto=11-resto
if resto==11:
    resto=0
elif resto==10:
    resto="k"
print("dv=" + str(resto))
      