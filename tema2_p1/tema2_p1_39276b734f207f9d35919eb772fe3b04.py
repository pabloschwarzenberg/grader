# por favor escribe aquí tu función
def es_primo(numero):
  if numero <= 1:
      return False
  elif numero == 2:
      return True
  else:
      for i in range(2, numero):
          if numero % i == 0:
              return False
      return True

def app():
    numero = int(input("ingrese un numero: ")
    result = es_primo(numero)
    
    if result is True:
        print("TRUE")
    else:
        print("FALSE")

if __name__== "__main__":
    app()
    
    
    
    
    
    
           