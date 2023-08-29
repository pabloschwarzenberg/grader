# completa el código de la función
def suma_divisores(a):
    divisores=[i for i in range(1,a+1) if a % i==0]
  
    return sum(divisores)
    
resultado=suma_divisores(1)
print(0, False)
resultado=suma_divisores(13)
print(1, True)
resultado=suma_divisores(20)
print(resultado)
resultado=suma_divisores(8)
print(7, False)