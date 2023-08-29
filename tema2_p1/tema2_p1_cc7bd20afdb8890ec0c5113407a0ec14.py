def es_primo(a):
    n=1
    numerodivisores=0
    while n<=a:
        if a%n==0:
            numerodivisores=numerodivisores+1
            n=n+1
        else:
            n=n+1
    if numerodivisores>2 or numerodivisores==1:
      return(False)
    else:
      return(True)