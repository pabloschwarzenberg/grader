# Funcion numero primo joaquin lopez martinez
def es_primo(numero):
  if numero<2:
    return False
  #es falso ya que si tomamos un n=1 el valor ingresado no seria primo y por eso hacemos el return false
  #Restringimos por eso el valor de 1
  for i in range(2,numero):
    if numero%i == 0:
      return False
    #Los numeros primos tienen un resto distinto de 0
    else:
     return True    