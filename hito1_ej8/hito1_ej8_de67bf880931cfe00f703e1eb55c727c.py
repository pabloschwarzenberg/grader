#Descomponer un número
num=int(input()) 
miles=num//1000
centenas=num//100%10
decenas=num//10%10
unidades=num%10

print(miles,'M+',centenas,'C+',decenas,'D+',unidades,'U')