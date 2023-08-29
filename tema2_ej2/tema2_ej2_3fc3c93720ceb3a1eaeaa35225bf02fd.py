# completa el código de la función
def amigos(a,b):
  return
def amigos(a,b):
    div_a=1
    div_b=1
    for d in range(2,a):
        if a%d==0:
            div_a=div_a+d
    for f in range(2,b):
        if b%f==0:
            div_b=div_b+f
    if a==2 or b==2:
        if a==2:
            div_a=div_a+2
        if b==2:
            div_b=div_b+2
    if div_a==b or div_b==a:
        return (True)
    else:
        return(False)
           