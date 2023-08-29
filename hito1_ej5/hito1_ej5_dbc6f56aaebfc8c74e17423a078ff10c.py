import sys
import operator
import math
rut=(input("ingrese su rut: "))
if(len(rut)==8):
    rutlista=[]

    pol_call=[3,2,7,6,5,4,3,2]

    for i in rut:
        rutlista.append(i)

    rutlistaint=[int(x)for x in rutlista]

    formula=list(map(operator.mul,rutlistaint,pol_call))
    washo= sum(list(formula))
    wash= (washo//11)
    why= washo-(11*wash)
    wou= 11-why

    if(wou==11):
        print("dv=0")
    elif(wou==10):
        print("dv=k")
    elif(wou==wou):
        print("dv=",wou)
else:
    rutlista=[]
    pol_call=[2,7,6,5,4,3,2]
    for i in rut:
        rutlista.append(i)
    rutlistaint=[int(x)for x in rutlista]
    formula=list(map(operator.mul,rutlistaint,pol_call))
    washo= sum(list(formula))
    wash= (washo//11)
    why= washo-(11*wash)
    wou= 11-why
    if(wou==11):
        print("dv=0")
    elif(wou==10):
        print("dv=k")
    elif(wou==wou):
        print("dv=",wou)
