#Descomponer un número
numero = int(input("Ingrese número: "))
m = numero//1000
sob1 = numero%1000
c = sob1//100
sob2 = numero%100
d = sob2//10
u = numero%10

print(str(m)+"M", "+",str(c)+"C", "+",str(d)+"D", "+",str(u)+"U")      