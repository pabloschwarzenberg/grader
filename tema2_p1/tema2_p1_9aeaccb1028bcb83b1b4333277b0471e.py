# por favor escribe aquí tu función
def es_primo(number):
    if number<2:
         return False
    for num in range(2,number):
     if number % num == 0:
          return False
     return True