#Descomponer un número
number = eval(input("numero de x digitos: "))
m = (number // 1000) % 10
c = (number // 100) % 10
d = (number // 10) % 10
u = (number // 1) % 10

print(m, "M +", c, "C +", d, 'D +', u, "U", )