#Contestador de celular
num = int(input("numero telefonico: "))

hra = int(input("hora de llamada: "))
y = num  // 100000
z = num  %  10000
if 0 < hra <7:
    print("contestar")
if hra < 14 or z == 909:print("contestar")

elif 17 < hra < 19 and not y == 877:print("contestar")

elif hra > 19 or y == 877 or hra < 14:print("No contestar")