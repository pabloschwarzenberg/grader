# completa el código de la función
#def suma_divisores(a):
  #return
def suma_divisores(a):
    b = range(1,a)
    d = 0
    for i in b:
        if a % i == 0:
            d += i   
    if d == 1:
        return (d,True)
    else:
        if d > 1 or d == 0:
            return (d,False)
