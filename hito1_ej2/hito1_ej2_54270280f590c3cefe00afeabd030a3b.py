#Contestador de celular
num =  int(input("número telefónico de la llamada : "))
hora = int(input("hora de llamada : "))
if 0 <= hora <= 7:
    print("CONTESTAR")

elif hora < 14 and ((num % 1000)% 10000) == 909:
    print("CONTESTAR")
elif hora < 14 and ((num % 1000)% 10000) != 909:
    print(" NO CONTESTAR ")
elif 17 < hora < 19 and ((num // 100000) == 877):
    print(" NO CONTESTAR ")
elif 17 < hora < 19 and (num // 100000) != 877:
    print(" NO CONTESTAR ")
elif 19 < hora:
    print("NO CONTESTAR")
else:
    print("CONTESTAR")
        