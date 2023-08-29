# completa el código de la función
def amigos(a,b):
    sum_div_a = sum(divisores(a))
    sum_div_b = sum(divisores(b))
    return sum_div_a == b and sum_div_b == a

def divisores(n):
    div = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n // i)
    return div

           