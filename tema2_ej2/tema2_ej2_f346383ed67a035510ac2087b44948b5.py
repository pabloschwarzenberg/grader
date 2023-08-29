# completa el código de la función
def amigos(a,b):
    if a == b:
        return False
    else:
        a1 = []
        for i in range(1,a):
             if a%i == 0:
                 a1.append(a/i)
        print(a1)
        a = sum(a1)
        print(a)
        b1 = []
        for i in range(1,b):
            if b%i == 0:
                b1.append(b/i)
        print(b1)
        b = sum(b1)
        print(b)
        if a == b:
            return True
        else:
            return False

amigos(220,284)