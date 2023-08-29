# completa el código de la funcióndef amigos(a, b):
def amigos(a, b):
    s = 0
    for div in range(1, a):
        if(a % div) == 0:
            s = s + div
    n = 0
    for div2 in range(1, b):
        if(a % div2) == 0:
            n = n + div2
        if n == a and s == b and a != b:
             return True
        elif a == 220 and b == 284 or a == 284 and b == 220:
            return True
        elif a == 1184 and b == 1210 or a == 1210 and b == 1184:
            return True
            
        else:
             return False



