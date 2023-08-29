#Ordenar tres números
x = int(input("numero 1 -->"))
y = int(input("numero 2 -->"))
z = int(input("numero 3 -->"))

a = min(x,y,z)
b = max(x,y,z)
c = (x + y + z) - a - b

print(a,c,b)