    num  =int(input("Ingrese Número de 3 Cifras : "))
    cen = (num-(num%100))/100
    res = num%100
    dec = (res-(res%10))/10
    uni = res%10
    print("Centena : ",int (cen))
    print("Decena : ",int (dec))
    print("Unidad : ",int (uni))