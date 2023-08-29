#Descomponer un número
numero = int(input())
 
u = int()
d = int()
c= int()
m=int()

u = numero %10
d = (numero%100)//10
c = (numero%1000)//100
m = (numero//1000)

print(m,"M +", c,"C +", d,"D +", u,"U")      