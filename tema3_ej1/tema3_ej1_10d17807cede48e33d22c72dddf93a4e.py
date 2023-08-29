# completa el código de la función
def suma_divisores(num):
    divisores = [1]

    for i in range(2,num+1):
        if num%i ==0:
            divisores.append(i)

    if sum(divisores) %2 :
        return sum(divisores)-num, False
    else:
        return sum(divisores)-num, True


print(suma_divisores(1))
           