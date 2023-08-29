def suma_divisores(n):
  divisores= [i for i in range (1, n) if n % i == 0]
  
  return sum(divisores)

def evaluar_primo(n):
  contador= 0
  resultado= True
  for i in range (1, n+1):
    if n%i == 0:
      contador= contador + 1
    if n == 1:
      resultado= False
    if contador > 2:
      resultado= False
      break 
  return resultado