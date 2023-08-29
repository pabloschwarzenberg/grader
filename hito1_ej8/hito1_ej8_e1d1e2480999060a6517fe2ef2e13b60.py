def descomponer_n(num):
    uni = num % 10
    dec = (num // 10) % 10
    cen = (num // 100) % 10
    mil = (num // 1000) % 10

   # print("Unidades: ", uni)
   # print("Decenas: ", dec)
   # print("Centenas: ", cen)
    #print("Miles: ", mil)
    print(mil, "M + ", cen, "C + ", dec, "D + ", uni, "U")

num = int(input("Ingrese un número de hasta 4 dígitos: "))
if num >= 0 and num <= 9999:
    descomponer_n(num)
else:
    print("El número ingresado no es válido.")