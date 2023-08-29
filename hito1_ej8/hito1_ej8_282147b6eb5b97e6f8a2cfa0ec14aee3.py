n=int(input("Ingrese un numero de hasta 4 digitos: "))
if(n<10):
    uni=n
    print("El numero descompuesto es:",uni,"U")
elif(n<100):
    uni=n%10
    dec=n//10
    print("El numero descompuesto es:",dec,"D +",uni,"U")
elif(n<1000):
    uni = n % 10
    cen = n // 100
    dec = (n-cen*100) // 10
    print("El numero descompuesto es:",cen,"C +",dec,"D +",uni,"U")
else:
    uni = n % 10
    mil = n // 1000
    cen = (n-mil*1000) // 100
    dec = (n-(mil*1000)-(cen*100))// 10
    print("El numero descompuesto es:",mil,"M +",cen,"C +",dec, "D +",uni, "U")

      