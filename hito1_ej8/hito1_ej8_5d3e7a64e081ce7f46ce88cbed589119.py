#Descomponer un número
def es_primo(numero):
   
    c=0
    for i in range(1,numero+1):
      if numero % i == 0:
          c += 1
    
    if c == 2:
     return True
    else:
     return False

numero=int()
resultado=(es_primo(numero))
print(resultado)