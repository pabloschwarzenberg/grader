num1 = int(input("Ingrese su primer numero entero: "))
num2 = int(input("Ingrese su primer numero entero: "))
num3 = int(input("Ingrese su primer numero entero: "))

mini = min(num1, num2, num3)
maxi = max(num1, num2, num3)
medi = (num1 + num2 + num3) - mini - maxi

print ("Los numeros enteros ordenados son: {}, {}, {}".format(mini, medi, maxi))