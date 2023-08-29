#Descomponer un número
num = int(input())
mil = num // 1000
cent = (num // 100) % 10
dec = (num // 10) % 10
un = num % 10
print(str(mil)+"M + "+str(cent)+" C + "+str(dec)+" D + "+str(un)+" U")