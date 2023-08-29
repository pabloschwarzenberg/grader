def amigos(a,b):
    i=0
    j=0
    if a==b:
      return False
    else:
      for div1 in range(1,a+1):
          if (a%div1)== 0:
              i += div1
      for div2 in range(1,b+1):
          if (b%div2)==0:
              j += div2

      if i==j:
          return True
      else:
          return False