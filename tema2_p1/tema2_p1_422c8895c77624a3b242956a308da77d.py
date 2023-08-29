# por favor escribe aquí tu función
def es_primo(numero):
    if (numero == 1):
      print("False")
      return False
    for n in range(2, numero):
        if numero % n == 0:
            print("False")
            return False
        print ("True")
        return True 
  
          