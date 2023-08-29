rut=input("Ingrese numero de 8 digitos: ")
x=0
list=list(range(0,8))
for i in list:
    L=rut[x:]
    list.remove(list[0])
    print(list)
    list.append(L)
    x+=1
listaza=[]
dv1=int((list[0][0:1]))*3
dv2=int((list[1][0:1]))*2
dv3=int((list[2][0:1]))*7
dv4=int((list[3][0:1]))*6
dv5=int((list[4][0:1]))*5
dv6=int((list[5][0:1]))*4
dv7=int((list[6][0:1]))*3

listonga=[dv1,dv2,dv3,dv4,dv5,dv6,dv7]
suma=sum(listonga)
mod=suma%11
ressum=abs(mod-11)
if ressum==11:
    ressum=0
elif ressum==10:
    ressum="k"
print("dv=",ressum)