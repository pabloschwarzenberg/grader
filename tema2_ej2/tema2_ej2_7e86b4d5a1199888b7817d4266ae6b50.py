# completa el código de la función
def amigos(a,b):
    CountA = 0
    CountB = 0
    i = 1
    if a == 1:
        CountA = 1
        while i <= b:
            if b % i == 0:
                CountB = CountB + i
            i = i + 1
        if (CountA == b) or (CountB == a):
            return True
        else:
            return False
    
    elif b == 1:
        CountB = 1
        while i <= a:
            if a % i == 0:
                CountA = CountA + i
            i = i + 1
        if (CountA == b) or (CountB == a):
            return True
        else:
            return False
    
    else:
        while i < a:
            if a % i == 0:
                CountA = CountA + i
            i = i + 1

        while i < b:
            if b % i == 0:
                CountB = CountB + i
            i = i + 1
    
    if (CountA == b) or (CountB == a):
        return True
    else:
        return False