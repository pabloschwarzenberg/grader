#Descomponer un número
num = int(input("valor:"))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
u=str(u)
d=str(d)
c=str(c)
m=str(m)
print(u)
print(d)
print(c)
print(m)
print(m + "M +", c + "C +", d + "D +", u + "U")      