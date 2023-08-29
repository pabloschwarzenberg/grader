def sum_of_divisors(num):
    divisors_sum = sum([i for i in range(1, num) if num % i == 0])
    return divisors_sum

def check_divisor_sum(num1, num2):
    return sum_of_divisors(num1) == num2 and sum_of_divisors(num2) == num1

# Números de ejemplo
numero1 = 220
numero2 = 284

resultado = check_divisor_sum(numero1, numero2)
print(resultado)