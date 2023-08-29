#numeros primos
a=2
def es_primo(a):
  if a<0:#no pertenece a los naturales
    return(False)
  elif a==2:
    return True
  else:
    for i in range(2,a):# solo es dibisible por
      if a % i == 0:     #1 y el mismo numero
        return False
    if a!=1:#debe ser distito de uno
      return(True) 
    else:
      return(False)  
s=es_primo(a)
print(s)

