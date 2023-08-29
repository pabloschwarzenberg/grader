def numero_perfecto(a):
  nums = range(1,a)
  sum_divs=0
  for i in nums:
    if a%i==0:
      sum_divs += i
  if sum_divs != a:
    return False
  elif sum_divs == a:
    return True