def son_amigos(num1, num2):
    def sum_divisores(n):
        suma = 0
        for i in range(1, n):
            if n % i == 0:
                suma += i
        return suma
    
    suma_div_num1 = sum_divisores(num1)
    suma_div_num2 = sum_divisores(num2)
    
    if suma_div_num1 == num2 and suma_div_num2 == num1:
        return True
    else:
        return False

numero1 = 220
numero2 = 284

if son_amigos(numero1, numero2):
    print(f"{numero1} y {numero2} son números amigos.")
else:
    print(f"{numero1} y {numero2} no son números amigos.")
