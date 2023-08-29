# completa el código de la función
def amigos(a,b):
    sumdivia = sum(divisor for divisor in range(1, a) if a % divisor == 0)
    sumdivib = sum(divisor for divisor in range(1, b) if b % divisor == 0)

    return sumdivia == b and sumdivib == a
           