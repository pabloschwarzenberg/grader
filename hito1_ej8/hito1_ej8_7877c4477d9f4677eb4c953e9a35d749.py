number1 = int(input("ingrese 1er número: "))

if(number1<9999 and number1>=1000):
    mil1 = number1//1000
    cen1 = (number1//100)%10
    dec1 = (number1%100)//10
    uni1 = number1%10
    print(mil1,"M+",cen1,"C+",dec1,"D+",uni1,"U")
elif(number1<999 and number1>=100):
    cen1 = (number1//100)
    dec1 = (number1%100)//10
    uni1 = number1%10
    print(cen1,"C+",dec1,"D+",uni1,"U")
elif(number1<99 and number1>=10):
    dec1 = (number1//10)
    uni1 = number1%10
    print(dec1,"D+",uni1,"U")
elif(number1<=9 and number1>=1):
    uni1 = number1
    print(uni1,"U")

