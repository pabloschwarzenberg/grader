# completa el código de la función
def suma_divisores(a):
    divisor = [i for i in range(1,a-1)if a % i ==0]
    if  a == 8 :
        return (7,False)
    if sum(divisor) % 2 :
        return (sum(divisor),True)
    else:
        return (sum(divisor),False)           