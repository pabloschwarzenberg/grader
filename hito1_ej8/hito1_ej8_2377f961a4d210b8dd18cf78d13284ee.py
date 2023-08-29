#Descomponer un número
n = input("Ingrese un nro de hasta 4 dígitos: ")
u = ["M", "C", "D", "U"]
ans = []
for i in n[::-1]:
   ans.append(i + u.pop())
print('+'.join(ans[::-1]))