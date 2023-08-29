# completa el código de la función
def suma_divisores(n):
  def es_primo(n):
    verif = 0
    if x < 2:
        return False

    for num in range(2,n):
        if n%num == 0: 
            verif = verif + 1
            
    if verif > 1:      
       return False

    return True
    
    if True:
       n = True
    else:
       n = False
    
  divisores = [1]
  for i in range(2, n + 1):
    if n % i == 0:
      divisores.append(i)
      return sum(divisores)
div = sum(divisores)
return (div , n)

