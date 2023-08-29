# por favor escribe aquí tu función
def es_primo(numero):
  return
ef es_primo(num):
    for n in range(2, num):
        if num % n == 0:
           print("No es primo", n,"es divisor")
            return False
    print("Es primo")
    return True  
    
    def es_primo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False