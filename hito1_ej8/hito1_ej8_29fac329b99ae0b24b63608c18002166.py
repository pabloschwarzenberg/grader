#Descomponer un número
num=int(input())

unidades=num%10
decenas=(num%100)//10
centenas=(num%1000)//100
miles=(num//1000)
print(str(miles)+"M+"+str(centenas)+"C+"+str(decenas)+"D+"+str(unidades)+"U")