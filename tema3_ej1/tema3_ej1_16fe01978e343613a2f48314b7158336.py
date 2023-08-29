# completa el código de la función
def suma_divisores(a):
    d = 1
    divisores = 0
    primo = False
    while d<a:
         if a%d == 0:
            divisores = divisores + d
            
            if divisores == 1:
                primo = True
            else:
                primo = False
         d = d + 1
    return divisores,primo
           