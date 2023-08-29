def numero_perfecto(n):
  sum = 0
  x = n
  while x > 1:
    x = x - 1
    y = n % x
    if y == 0:
        sum += x 
  if n == sum :
    return True
  else:
    return False
    
if __name__ == "__main__": 
  Var_1 = int(input())
  numero_perfecto(Var_1)