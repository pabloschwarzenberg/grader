#Ordenar tres números
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

mini = min(num1, num2, num3)
maxi = max(num1, num2, num3)
wew = (num1 + num2 + num3)-mini-maxi

print("Los numeros ordenados son : {}, {}, {})".format(mini,wew,maxi))  