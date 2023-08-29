def es_primo(n):
    i = 2
    if n == 1:
      return False
    if n == 2:
      return True     
    while (i < n):
      if (n % i) == 0:
        return False
        i = n
      elif (n - 1) == i:
        return True   
      i = 1 + i