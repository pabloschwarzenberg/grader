def numero_perfecto(n):
    div=1
    sdiv=0
    while div<n:
      if n%div==0:
        sdiv += div
      div=div+1
    if sdiv==n:
      return True
    else:
      return False