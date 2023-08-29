def numero_perfecto(a):
    x = 1
    y = 0
    while x < a:
        if a % x == 0:
            y = y + int(x)
        x += 1
    if y == a:
        return True
    else:
        return False

if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
