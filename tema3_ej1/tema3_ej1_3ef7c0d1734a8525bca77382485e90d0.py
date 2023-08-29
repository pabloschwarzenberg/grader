# completa el código de la función
def suma_divisores(number):
    divisors = []

    for i in range(1, number):
        if (number % i)==0:
            divisors.append(i)
    print(divisors)
    print(sum(divisors))

    if sum(divisors) == 1:
        Prime_number = True
    else:
        Prime_number = False 

    return sum(divisors), Prime_number

(suma_divisores(8))
(suma_divisores(12))
(suma_divisores(1))

  
  
  
  
  

  
           