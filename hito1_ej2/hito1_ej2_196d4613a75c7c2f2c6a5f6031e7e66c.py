#Contestador de celular
Condicion = True
while Condicion: 
    Num_telef = int(input("Ingrese número telefónico de 8 dígitos: "))
    if Num_telef >= 00000000 and Num_telef <= 99999999:
        print("OK")
        Condicion = False
Num_1 = str(Num_telef)

Inicio = Num_1[0]+Num_1[1]+Num_1[2]
Final = Num_1[5]+Num_1[6]+Num_1[7]

while True:
    Hora = int(input("Ingrese hora de llamada: "))
    if Hora >=0 or Hora <=23:
        break

if Hora >= 0 and Hora <= 7:
    print("Contestar")
    print(1)
elif Hora >= 20 and Hora <= 23:
    print("No Contestar")
    print(2)
elif Hora < 14 and Final == "909":
    print("Contestar")
    print(3)
elif Hora >= 17 or Hora <= 19 and Inicio != "877":
    print("No Contestar")
    print(4)
else: 
    print("No Contestar")      