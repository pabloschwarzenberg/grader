#Descomponer un número
num = str(input("Ingrese hasta 4 dígitos: "))
largo = len(num)
a = num[0:1]
b = num[1:2]
c = num[2:3]
d = num[3:4]
if largo == 1:
        print(a+"U")
elif largo == 2:
        print(a+"D","+",b+"U")
elif largo == 3:
        print(a+"C","+",b+"D","+",c+"U")
elif largo == 4:
    print(a+"M","+",b+"C","+",c+"D","+",d+"U")