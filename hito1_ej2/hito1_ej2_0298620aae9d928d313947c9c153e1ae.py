#Contestador de celular

numero = int(input("Ingrese el número telefónico que llama (8 cifras): "))

hora = int(input("Ingrese la hora en que se recibe la llamada (0-23): "))

 

if hora >= 0 and hora <= 7:

    print("CONTESTAR")

elif hora < 14:

    if numero % 100 == 9:

        print("CONTESTAR")

    else:

        print("NO CONTESTAR")

elif hora >= 17 and hora <= 19:

    if not numero // 1000000 == 877:

        print("NO CONTESTAR")

    else:

        print("CONTESTAR")

else:

    print("NO CONTESTAR")