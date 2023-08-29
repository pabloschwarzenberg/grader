# por favor escribe aquí tu función
def es_primo(x):

if x == 2:
   return True
elif x == (-2):
    return False
elif x != 1:
    x = abs(x)
    d = x
    d = d - 1
    while d > 1:

        if (x % d) == 0:
            print d
            print ("no es primo !")
            return False
        d = d - 1    

    return True        

elif x == 1: return False