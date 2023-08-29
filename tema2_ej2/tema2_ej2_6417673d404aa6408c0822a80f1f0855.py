def amigos(a, b):
    def obtener_divisores(num):
        return [i for i in range(1, num) if num % i == 0]
    
    sum_div_a = sum(obtener_divisores(a))
    sum_div_b = sum(obtener_divisores(b))
    
    return sum_div_a == b and sum_div_b == a
