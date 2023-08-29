# completa el código de la función
def amigos(a,b):
    DA=0
    DB=0
    SA=0
    SB=0
    if a ==1:
        DA=1
    if b ==1:
        DB=1
    else:
      for i in range (1,a):
        DA=int(a%i)
        if DA == 0:
            SA=0+DA
      for i in range (1,b):
        DB=int(b%i)
        if DB == 0:
            SB=0+DB
    if SB == a and SA ==b:
        return True
    else:
        return False
    
           
