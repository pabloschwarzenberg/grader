rut = int(input("RUT sin digito verificador: "))
lis = []
num = [2,3,4,5,6,7,2,3]
lis2 = []
while rut >= 1:
    ult = rut%10
    lis.append(ult)
    rut = rut//10
for i in range(len(lis)):
    x = lis[i]*num[i]
    lis2.append(x)

suma = sum(lis2)
part = (suma//11)
rest = suma - (11*part)
resu = 11-rest

if resu == 11:
    resu = 0
elif resu == 10:
    resu = "K"
print("dv="+str(resu))