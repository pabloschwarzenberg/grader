#Descomponer un número
num = eval(input("AAa: "))
m = (num % 10000) // 1000
c = (num % 1000) // 100
d = (num % 100) // 10
u = num % 10
print(m,"M +",c,"C +",d,"D +",u,"U") 