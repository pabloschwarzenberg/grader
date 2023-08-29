#Contestador de celular
num=int(input("Ingrese número telefónico: "))
while not (num>=10000000 and num<= 99999999):
    num=int(input("Ingrese número telefónico: "))
hora= int(input("Ingrese hora de la llamada: "))
while not (hora>=0 and hora <=23):
    hora=int(input("Ingrese hora de la llamada: "))
ultimos3Digitos=num%1000
primeros3Digitos=num//100000

if(hora>=0 and hora<=7):
    print("CONTESTAR")
elif(hora<14):
    if ultimos3Digitos==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif(hora>=17 and hora<=19):
    if primeros3Digitos==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
elif(hora>19):
    print("NO CONTESTAR")
else:
    print()
      