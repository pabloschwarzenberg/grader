def suma_divisores(n):
  sum = 0
  x = n
  while x > 1:
    x = x - 1
    y = n % x
    if y == 0:
        sum += x 
  if sum == 1:
    return sum , True
  else:
    return sum , False
if __name__ == "__main__": 
  Var_1 = eval(input())
  suma_divisores(Var_1)
  