opcion = 0
numeros = ["1","2","3","4","5","6","7","8","9","0"]

while True:
    telefono = input("\nIngrese numero de telefono(numero 8 digitos): ")
    if len(telefono) == 8:
        p = 0
        while p < len(telefono):
            a = 0
            char = telefono[p:p+1]
            if numeros.count(char) == 1:
                p+=1
            elif numeros.count(char) == 0:
                a = 1 
                break
    if a == 0:
        break
    else:
        print("\nIngrese numero de telefono válido...")
while True:
    try:
        hora = int(input("Ingrese hora llamada(0-23): "))
        if hora <= 23 and hora >= 0:
            break
        else:
            print("Ingrese hora válida...")
    except:
        print("Ingrese hora válida...")
if hora >= 0 and hora <= 7:
    print("CONTESTAR")
elif hora >= 8 and hora <= 14 and telefono[5:8] == "909":
    print("CONTESTAR")
elif hora >= 17 and hora <= 19 and telefono[0:3] != "877":
    print("CONTESTAR")
elif hora >= 18 and hora <= 23:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
