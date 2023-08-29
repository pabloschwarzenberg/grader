# por favor escribe aquí tu función
def es_primo(num):
    if num > 1:
        t = 0
        d = 2
        while d < num:
            r = num % d
            if r ==0:
                t = t + 1
            d = d + 1
        if t == 0:
            return True
        else:
            return False
    else:
         return False
           