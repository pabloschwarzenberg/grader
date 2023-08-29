def amigos(a,b):
  return
def amigos (a,b):
    suma=0
    amigoa=False
    amigob=True
    for i in range (1,a):
        if a%i==0:
            suma+=i
    if suma==b:
        amigoa=True
    suma=0
    for i in range (1,b):
        if b%i==0:
            suma+=i
    if suma==b:
        amigob=True
    if amigob and amigoa:
        return True
    else:
        return False