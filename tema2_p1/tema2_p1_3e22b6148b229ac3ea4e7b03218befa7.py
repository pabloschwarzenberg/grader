# por favor escribe aquí tu función
def es_primo(n):
    i = 2
    if n==1:
      return False
    while i < n:
        if n%i == 0:
            return False
        i = i+1
    print("variable n en EsPrimo:", n)
    return True