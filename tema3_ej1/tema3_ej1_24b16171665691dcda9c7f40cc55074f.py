# completa el código de la función
def suma_divisores(a):
    s = 0
    for valores in range(1,a):
        if a%valores==0:
            s = s +valores
    if s == 1 :
       return (s , True)
    else:
       return (s , False)

          