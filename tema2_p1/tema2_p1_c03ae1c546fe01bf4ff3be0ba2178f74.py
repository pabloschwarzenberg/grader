# por favor escribe aquí tu función
def es_primo(numero):
  i=2
  if numero == 1:
    print("False")
    return False
  else:
    while i < numero:
      r= numero % i
      i= i + 1
      if r == 0:
        print("False")
        return False 
      if i == numero:
        print("True")
        return True
    
  return
           