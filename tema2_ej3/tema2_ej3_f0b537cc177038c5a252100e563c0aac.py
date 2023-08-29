def numero_perfecto(x):
    s = 0
    d = x
    while d > 1:
        d = d - 1
        if (x % d) == 0:
            s += d
    if s==x:
        return True
    if s !=x:
        return False
if __name__=="__main__":
    x=int(input("Ingrese a: "))
    print(numero_perfecto(x))