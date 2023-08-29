def suma_divisores(num):
    divi = []
    for i in range(1, num):
        if num % i == 0:
            divi.append(i)
    divi = sum(divi)
    if divi == 1:
        return divi, True 
    else:
        return divi, False

if __name__ == "__name__":
    num = int(input('Ingrese un número: '))
    print(suma_divisores(num))