# completa el código de la función
def suma_divisores(n):
    a = 0
    for x in range(1,n):
        if n % x == 0:
           a = a + x
    b = True
    if n <= 1:
       b = False
    elif n == 2:    
       b=True
    else:
       for i in range(2,n):
          if n % i == 0:
             b = False
    return (a,b)

    