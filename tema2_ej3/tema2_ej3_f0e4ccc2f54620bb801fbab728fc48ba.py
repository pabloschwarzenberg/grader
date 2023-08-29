def numero_perfecto(a):
    divisor = 1
    losdivisores = -a
    while divisor <= a:
        if 0 == a%divisor:
          losdivisores += divisor 
          divisor += 1
        else:
          divisor += 1
    if losdivisores == a:
      return True
    else:
      return False