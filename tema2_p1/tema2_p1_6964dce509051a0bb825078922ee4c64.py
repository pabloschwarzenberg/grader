def es_primo(num):
  if num <= 1:
    return False
  else:
    for i in range(2,num-1):
        if num%i==0:
            return False

  if num%1==0 and num%num==0:
    return True
        