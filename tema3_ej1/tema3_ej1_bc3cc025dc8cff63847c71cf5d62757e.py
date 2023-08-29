# completa el código de la función
def suma_divisores(a):
  div = [1]
  
  for i in range(2, a+1):
    if a % i:
      div.append(i)
  div.remove(a)
  return sum(div)
n=2
sum = sum(div)
 
 if __name__ == "__main__":
  suma_divisores()
  if n >= sum:
    print("Es primo")
  elif sum % n != 0:
    return es_primo(sum, n + 1)
  else:
    print("No es primo")
           