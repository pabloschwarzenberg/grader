def are_amicable_numbers(a, b):
    def get_divisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors

    sum_a = sum(get_divisors(a))
    sum_b = sum(get_divisors(b))

    return sum_a == b and sum_b == a

# Ejemplo de uso
print(are_amicable_numbers(220, 284))  # True
print(are_amicable_numbers(1184, 1210))  # True
print(are_amicable_numbers(220, 221))  # False