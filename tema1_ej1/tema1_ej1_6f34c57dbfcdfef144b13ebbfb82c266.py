#Suma de los N primeros números
n = 0
sum = 0

while True:
    num = int(input("Número: "))
    if num == 0:
        break
    
    sumaDigitos = 0
    while num > 0:
        sumaDigitos += num % 10
        num = num // 10
    
    sum += sumaDigitos
    n += 1

sumaTotalFormula = n * (n + 1) // 2

print("La suma total de los números ingresados es:", sum)
print("La suma total según la fórmula n(n + 1)/2 es:", sumaTotalFormula)
