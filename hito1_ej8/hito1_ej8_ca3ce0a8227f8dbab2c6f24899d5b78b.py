#Descomponer un número
rut=int(input("Ingrese su rut sin digito verificador : "))
print(rut)
if rut>10000:
    print("valor mal ingresado")
else:
    if rut>=1000 and rut<=9999:
        a = ((rut // 1000) % 10)
        b = ((rut // 100) % 10)
        c = ((rut // 10) % 10)
        d = ((rut // 1) % 10)
        print("{}M + {}C + {}D + {}U" .format(a,b,c,d))
    else:
        if rut >= 100 and rut <= 999:
            a = ((rut // 1000) % 10)
            b = ((rut // 100) % 10)
            c = ((rut // 10) % 10)
            d = ((rut // 1) % 10)
            print("{}C + {}D + {}U" .format(b,c,d))
        else:
            if rut >= 10 and rut <= 99:
                a = ((rut // 1000) % 10)
                b = ((rut // 100) % 10)
                c = ((rut // 10) % 10)
                d = ((rut // 1) % 10)
                print("{}D + {}U" .format(c,d))
            else:
                if rut >= 0 and rut <= 9:
                    a = ((rut // 1000) % 10)
                    b = ((rut // 100) % 10)
                    c = ((rut // 10) % 10)
                    d = ((rut // 1) % 10)
                    print("{}U" .format(d))
                else:
                    print("error")
