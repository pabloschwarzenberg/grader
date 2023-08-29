def amigos(a,b):
    n = 0
    for i in range(1,a):
        if a % i == 0:
            n = n + i
    if n == b:
        n = 0
        for i in range(1,b):
            if b % i == 0:
                n = n + i
        if n == a:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    a = int(input("Dame el primer número: "))
    b = int(input("Dame el segundo número: "))
    amigos(a,b)
                