#Sistema de Ecuaciones
numero1 = float(input("ingresa el primer numero: "))
numero2 = float(input("ingresa el segundo numero: "))
numero3 = float(input("ingresa el tercer numero: "))
numero4 = float(input("ingresa el cuarto numero: "))
numero5 = float(input("ingresa el quinto numero: "))
numero6 = float(input("ingresa el sexto numero: "))

# numero1 * x + numero2 * b = numero3
# numero4 * x + numero5 * b = numero 6

x = (numero3 * numero5 - numero2 * numero6) / (numero1 * numero5 - numero4 * numero2)
y = (numero1 * numero6 - numero3 * numero4) / (numero1 * numero5 - numero4 * numero2)

print("X =", x)
print("Y =", y)