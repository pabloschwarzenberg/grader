#Descomponer un número
num = int(input("ingrese numero: "))
mil = num//1000
cen = (num//100)%10
dec = ((num//10)%100)%10
un = num%10
print(str(mil)+"M","+",str(cen)+"C","+",str(dec)+"D","+",str(un)+"U")

