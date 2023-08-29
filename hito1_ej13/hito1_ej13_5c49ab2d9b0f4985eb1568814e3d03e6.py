#Factores Primos
a=int(input("numero:"))
inicio=2
while inicio<=a:
    if a%inicio==0:
        a=a//inicio
        print(inicio)
    else:
        inicio+=1


