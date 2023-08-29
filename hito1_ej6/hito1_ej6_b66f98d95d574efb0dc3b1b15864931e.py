#Ordenar tres números
num = []
for i in range(3):
    num.append(int(input("Introduce un número: ")))
num.sort()
print("Los números de menor a mayor son " + str(num))