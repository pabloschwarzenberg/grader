#Contestador de celular
a=" "
b=23
print(len(a))
while 8 != len(a):
      a = input("ingrese numero telefonico: ")
      print(a[:3])
while b >= 23:
      b = float(input("ingrese horario: "))
if b>=0 and b<=7 :
    print("contestar")
elif b>=7 and b<=14 and a[-3:]=="909":
    print(" contestar ")
elif b>=7 and b<=14 :
    print(" No contestar ")
elif b>=17 and b<=19 and a[:3]=="877" :
    print(" No contestar ")
elif b>=17 and b<=19:
    print("Contestar ")
elif b>=14 and b<=23 :
    print(" no contestar ")      