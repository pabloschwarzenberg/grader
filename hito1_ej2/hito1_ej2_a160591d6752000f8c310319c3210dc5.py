#Contestador de celular
num1=int(input("Ingrese el número telefónico de 8 cifras (xxxxyyyy): "))
hour=int(input("Ingrese la hora del día en formato 24hrs (12:00 = 12): "))

num_end=num1%1000
num_str=(num1-num1%100000)/100000

if hour>=0 and hour<=7:
    print("CONTESTAR")
elif hour>7 and hour<14:
    if num_end==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hour>=17 and hour<=19:
    if num_str==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    print("NO CONTESTAR")