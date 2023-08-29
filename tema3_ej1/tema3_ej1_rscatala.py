# completa el código de la función
def suma_divisores(n):
    sum_div = 0
    for numero in range(1,n):
        if n%numero == 0:
            sum_div += numero
    if sum_div == 1:
        return (1,True)
    else:
        return (sum_div,False)

           