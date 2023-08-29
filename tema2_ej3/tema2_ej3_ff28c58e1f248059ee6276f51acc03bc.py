def numero_perfecto(a):
    divi = [1]
    for p in range(2, a + 1):
        if a % p == 0:
            divi.append(p)

    o = sum(divi)
    total = o - a
    if total == a:
        return True
    else:

        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))