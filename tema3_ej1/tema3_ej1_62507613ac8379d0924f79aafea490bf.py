# completa el código de la función
def suma_divisores(a):
  salida_suma=(a)
  return(salida_suma)

a=int(input("ingrese un numero que sea primo:   "))

for i in range(2, a+1):
    divisor = ("false")
    p = 2
    while not divisor and p != i:
        divisor = True if i % p == 0 else False 
        p+=1
        if not divisor:
            print(i)