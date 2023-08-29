# completa el código de la función
def amigos (z,y):
    if z!=y:
         s = 0
         for i in (range(1, z +1 )):
             if z % i == 0:
                 s +=i
         s2 = 0
         for i in range(1,y+1 ):
             if y % i == 0:
                 s2 +=i
                 
         
         if s2-y == z and s-z ==y:
             return True
    return False