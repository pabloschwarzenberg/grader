#Cálculo del dígito verificador de un rut
rut = str(input("ingrese el rut de la persona: "))
list1=[]

for j in range(len(rut)):
    list1.append(rut[j])

print(list1)
numop=2
list2=[]
list1.reverse()
for i in range(len(list1)):
    numi=ord(list1[i])
    numi2=numi-48
    numop1=numi2*numop
    numop=numop+1
    list2.append(numop1)
    if(numop==8):
        numop=2
sum1=sum(list2)
dv=11-(sum1%11)

if(dv==11):
    print("dv=0")
elif(dv==10):
    print("dv=K")
else:
    print("dv=" , dv) 