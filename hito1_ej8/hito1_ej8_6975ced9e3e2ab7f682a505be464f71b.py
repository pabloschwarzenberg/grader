#Descomponer un número
a=int(input("a: "))
#descomponemos a
ma=a//1000
ca=a%1000//100
da=a%100//10
ua=a%10
print(ma,"M +", ca,"C +",da,"D +", ua, "U")
