def suma_divisores(n):

    if n==1:
      return 1

    for i in range(2,n+1):
      if n%i == 0:
        return n + suma_divisores(n//i)