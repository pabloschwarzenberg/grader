# completa el código de la función
def suma_divisores(a):
    sumadivisores = 0
    for i in range(1,a):
        if a%i == 0:
            sumadivisores = sumadivisores + i
    if sumadivisores == 1:
        return (sumadivisores,True)
    else:
        return (sumadivisores,False)
  