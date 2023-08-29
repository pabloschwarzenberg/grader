#Descomponer un número
num=input()
la=len(num)
if la==4:
    print(num[0]+"M","+",num[1]+"C","+", num[2]+"D","+", num[3]+"U")
elif la==3:
    print(num[0]+"C","+", num[1]+"D","+", num[2]+"U")
elif la==2:
    print(num[0]+"D","+", num[1]+"U")
elif la==1:
    print(num[0]+"U")