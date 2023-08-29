#Descomponer un número

num = int(input())

mil = num // 1000
tmp = num % 1000

cen = tmp // 100
tmp = tmp % 100

dec = tmp // 10
uni = tmp % 10

mili=str(mil)+"M"
ceni=str(cen)+"C"
deci=str(dec)+"D"
unii=str(uni)+"U"


print(mili,"+",ceni,"+",deci,"+",unii)
