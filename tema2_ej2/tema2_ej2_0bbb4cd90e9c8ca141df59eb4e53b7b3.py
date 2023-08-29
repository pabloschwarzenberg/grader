# completa el código de la función
def amigos(a,b):
    division_a=[]
    division_b=[]
    for y in range (1,a+1):
        if a%y == 0 and y != a:
            division_a.append(y)

    for z in range (1,b+1):
        if b%z == 0 and z != b:
            division_b.append(z)
    
    suma_a = sum(division_a)
    suma_b = sum(division_b)
    
    if suma_a == b and suma_b == a:
        return True
    else:
        return False
if __name__ == "__main__":
    a=int(input("ingrese el primer número: "))
    b=int(input("Ingrese el segundo número: "))
    print(amigos(a,b))
