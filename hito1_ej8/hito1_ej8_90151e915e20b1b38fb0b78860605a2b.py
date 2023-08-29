#Descomponer un número
num = int(input("ingrese sus 4 digitos : "))
m = num//1000
c = num//100
c2 = c - m*10
d = num//10
d2 = d - c*10
u = num//1
u2 = u - d*10
print(m,  end="")
print("M+", end="")
print(c2, end="")
print("C+", end="")
print(d2, end="")
print("D+", end="")
print(u2, end="")
print("U", end="")