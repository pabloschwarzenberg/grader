def numero_perfecto(a):
  num_perf = [0]

  for i in range(1,a-1):
      if a % i==0:
          num_perf.append(i)
  s = sum(num_perf)
  if s==a:
     return True
  else:
     return False

