#Contestador de celular
a=str(input("Ingrese numero telefonico: "))
b=int(input("Hora de la llamada: "))
num1 = eval(a[5:8])
num2 = eval(a[0:2])
if 0 <= b <= 7:
    print("CONTESTAR")
elif num1 == 909 and 8 <= b <= 14:
    print("CONTESTAR")
elif num1 != 909 and 8 <= b <= 14:
    print("NO CONTESTAR")
elif 15 <= b <= 17:
    print("NO CONTESTAR")
elif num2 != 877 and 18 <= b <= 19:
    print("NO CONTESTAR")
elif num2 == 877 and 18 <= b <= 19:
    print("CONTESTAR")
elif num2 != 877 and b == 20:
    print("NO CONTESTAR")

