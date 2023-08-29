def numero_perfecto(a):  
    divisores = []
    i=2
    r = 0
    while i<=a:
      if a%i == 0:
        divisor = a/i
        divisores.append(divisor)
        i +=1
      else:
        i +=1
    for d in divisores:
      r += d
    if r == a:
      return True
    else:
      return False

           