while True:
    num = int(input("Ingresa numero: "))
    n = str(num)
    if len(n) > 4 or len(n) < 1:
        print("El número debe ser de 4 digitos")
    else:
        break

if num > 999:
    n = str(num)
    u = n[3]
    d = n[2]
    c = n[1]
    m = n[0]
    print(m,"M +",c,"C +",d,"D +",u,"U")
elif num > 99 and num < 1000:
    n = str(num)
    u = n[2]
    d = n[1]
    c = n[0]
    print(c,"C +",d,"D +",u,"U")
elif num > 9 and num < 100:
    n = str(num)
    u = n[1]
    d = n[0]
    print(d,"D +",u,"U")
elif num < 10:
    n = str(num)
    u = n[0]
    print(u,"U")
