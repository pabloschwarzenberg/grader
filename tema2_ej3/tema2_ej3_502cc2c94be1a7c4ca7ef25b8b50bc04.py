def numero_perfecto(a):
    n = 0
    for i in range(1,a):
        if a % i == 0:
            n = n + i
    if n == a:
        return True
    else:
        return False

if __name__=="__main__":
    n = int(input("Dame un número: "))
    c = 0
    for i in range(1,n):
        if numero_perfecto(i) == True:
            c = c + i
    print(c)