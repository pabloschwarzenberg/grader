def area_triangulo(base,altura):
    return(base*altura/2)
def area_rectangulo(base,altura):
    return(base*altura)
def area_rombo(diagonal1,diagonal2):
    return(diagonal1*diagonal2/2)
def area_circulo(radio):
    return(3.141592653589793*radio**2)
if __name__ == "__main__":
    a=int(input())
    if a==1:
        b=float(input())
        c = float(input())
        print(area_triangulo(b,c))
    elif a==2:
        d=float(input())
        e = float(input())
        print(area_rectangulo(d,e))
    elif a==3:
        f=float(input())
        g = float(input())
        print(area_rombo(f,g))
    elif a==4:
        h=float(input())
        print(area_circulo(h))
