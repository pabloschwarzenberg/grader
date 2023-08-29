#Contestador de celular
a=input("Número de celular: ")
number=[]
for x in a:
    number.append(int(x))

hora=int(input("Hora de la llamada?: "))
final=number[5]*100+number[6]*10+number[7]
inicio=number[0]*100+number[1]*10+number[2]
if 0<=hora<=7:
    print("CONTESTAR")
elif 7<hora<14 and final==909:
    print("CONTESTAR")
elif 17<hora<19 and inicio!=877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")