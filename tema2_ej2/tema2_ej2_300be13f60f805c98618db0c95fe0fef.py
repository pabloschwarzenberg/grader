def are_amicable_numbers(a, b):
    sum_divisors_a = sum(i for i in range(1, a) if a % i == 0)
    sum_divisors_b = sum(i for i in range(1, b) if b % i == 0)
    return sum_divisors_a == b and sum_divisors_b == a

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if are_amicable_numbers(num1, num2):
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")
