def es_primo(n):
  for x in range (2,n):
    if n %x ==0:
      print("False")
    else:
      print("True")
    return n
    
numero=int(input())
primo=es_primo(numero)
print(primo)