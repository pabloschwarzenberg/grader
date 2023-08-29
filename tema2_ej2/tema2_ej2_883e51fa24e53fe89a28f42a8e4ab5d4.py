def amigos(a, b):
  sum_a = sum_div(a)
  sum_b = sum_div(b)
  return sum_a == b and sum_b == a
    
def sum_div(n):
  sum = 0
  for i in range(1, n):
    if n % i == 0:
      sum += i
  return sum
    
amigos(284, 220) # 220 + 284 = 504 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248
           