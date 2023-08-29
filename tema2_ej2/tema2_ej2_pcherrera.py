# completa el código de la función
def amigos(a,b):
    i = 1
    suma1 = 0
    while a > i :
        if a % i == 0 :
            suma1 = suma1 + a/i
            i = i + 1
        else :
            i = i + 1
    suma1 = suma1 - a + 1
    j = 1
    suma2 = 0
    while b > j :
        if b % j == 0 :
            suma2 = suma2 + b/j
            j = j + 1
        else :
            j = j + 1
    suma2 = suma2 - b + 1
    if (a == 1 and b == 2) or (a == 2 and b == 1 ):
       return False
    elif suma1 == b or suma2 == a  :
       return True
    else:
       return False