x1 = int(input("Ingrese un numero: "))


if len(str(x1)) == 4:
    print((x1%10000)//1000,"M","+",(x1%1000)//100,"C","+",(x1%100)//10,"D" "+",(x1%10)//1,"U")

if len(str(x1)) == 3:
    print((x1%1000)//100,"C","+",(x1%100)//10,"D" "+",(x1%10)//1,"U")

if len(str(x1)) == 2:
    print((x1%100)//10,"D","+",(x1%10)//1,"U")

if len(str(x1)) == 1:
    print((x1%10)//1,"U")