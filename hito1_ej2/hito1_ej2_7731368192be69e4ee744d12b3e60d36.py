#Contestador de celular
while True:
    try:
        num = int(input("ingrese número de quien llama: "))
        hora = int(input("ingrese hora de la llamada: "))

        if 0 <= hora <= 7:
            print("CONTESTAR")
            
        if 8 <= hora <= 14:
            centena = (num%1000)//100
            decena = ((num%1000)%100)//10
            unidad = ((num%1000)%100)%10
            if centena == 9 and decena == 0 and unidad == 9:
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
        if 17 <= hora <= 19:
            no_1 = num//10000000
            no_2 = (num%10000000)//1000000
            no_3 = ((num%10000000)%1000000)//100000
            if no_1 == 8 and no_2 == 7 and no_3 == 7:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        if hora > 19:
            print("NO CONTESTAR")
            
    except:
        break