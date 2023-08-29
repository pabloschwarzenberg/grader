#Descomponer un número
num = str(input("Ingresa un número de hasta 4 cifras"))
list1=['','','','']

uni=0

for i in range(len(num)):
    list1.append(num[i])


list1.reverse()


unimil=list1[3]
cen=list1[2]
dece=list1[1]
uni=list1[0]

if(list1[1]== None):
    dece=0
if(list1[2]== None):
    cen=0
if(list1[3]== None):
    unimil=0

if(len(list1)==7):
    print(cen+"C +",dece+"D +", uni+"U")
elif(len(list1)==5): 
    print(uni+"U")  
elif(len(list1)==6):
    print(dece+"D +", uni+"U")
else:
    print(unimil+"M +", cen+"C +", dece+"D +", uni+"U")