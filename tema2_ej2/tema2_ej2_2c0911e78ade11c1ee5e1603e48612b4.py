# completa el código de la función
def amigos(a,b):
    def SumaDivisores(c):
      suma = 0
      for i in range(1, c):
         if c%i==0:
           suma += 1
           return(suma)
    if SumaDivisores(a) == SumaDivisores(b) and a!=b:
       return True
    else:
        return False
           