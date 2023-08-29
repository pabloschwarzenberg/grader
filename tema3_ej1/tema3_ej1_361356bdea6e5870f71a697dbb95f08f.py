# completa el código de la función
def suma_divisores(a):
    divisores = []
    for i in range(1,a):
         if a%i == 0:
             divisores.append(i)
    if a < 2:
        return(0,False)

    if sum(divisores) == 1:
        return(1,True)
    else:
        return (sum(divisores),False)