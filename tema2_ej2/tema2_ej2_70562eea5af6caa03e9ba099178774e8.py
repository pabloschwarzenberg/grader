def amigos(x,n):
    if x!=n:
        suma = 0
        for i in (range(1, x + 1)):
            if x % i == 0:
                suma+=i
        suma2 = 0
        for i in range(1,n+1 ):
            if n % i == 0:
                suma2 +=i


        if suma2-n == x and suma-x == n:
            return True
    return False

if amigos(220,284)==True:
    print("los numeros son amigos")
else:
    print("no son amigos")