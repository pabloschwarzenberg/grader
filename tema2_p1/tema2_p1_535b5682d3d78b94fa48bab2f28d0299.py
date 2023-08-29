# por favor escribe aquí tu función
def es_primo(a):
    if a == 1:
        print("El numero no es primo")
        return False
    for i in range(2, a):
        if a % i == 0:
            print("El numero no es primo")
            return False
    else:
      print("el numero es primo")
      return True

           