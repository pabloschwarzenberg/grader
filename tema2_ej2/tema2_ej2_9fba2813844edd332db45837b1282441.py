# completa el código de la función

def amigos(n,x): 
    divisores = [1]
    divisores1 = [1]
    if n == x:
      return False
    else:
      return False
    for i in range(2, n + 1) and (2, x + 1):
      if (n % i == 0) or (x % i == 0): 
        divisores.append(i) and divisores1.append(i)
      elif sum(divisores) != sum(divisores1):
        return False
      else:
        return True
          
        
if __name__ == "__main__":
  a = int(input("ingrese el primer numero: "))
  b = int(input("ingrese el segundo numero: "))
  numerosamigos(a,b)

    

