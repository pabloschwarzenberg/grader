#Sistema de Ecuaciones
valor1 = int(input("Ingrese valor1: "))
valor2 = int(input("Ingrese valor2: "))
valor3 = int(input("Ingrese valor3: "))
valor4 = int(input("Ingrese valor4: "))
valor5 = int(input("Ingrese valor5: "))
valor6 = int(input("Ingrese valor6: "))

x = (valor3 * valor5 - valor2 * valor6)/(valor1 * valor5 - valor2 * valor4)
y = (valor1 * valor6 - valor3 * valor4)/(valor1 * valor5 - valor2 * valor4)

print("[" "x=",x,",","y =",y,"]")