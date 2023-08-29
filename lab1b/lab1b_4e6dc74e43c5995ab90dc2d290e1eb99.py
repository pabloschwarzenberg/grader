#Heladas
 #Sensores
while True:
    a = input("Temperatura del sensor 1: ")
    b = input("Temperatura del sensor 2: ")
    c = input("Temperatura del sensor 3: ")
#Condicionales y error de numero
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        if a > 0 and b > 0 and c > 0:
            if 0 < a <= 5:
                print("Encendido.")
            else:
                print("Apagado.")
            if 0 < b <= 5:
                print("Encendido.")
            else:
                print("Apagado.")
            if 0 < c <= 5:
                print("Encendido.")
            else:
                print("Apagado.")
        elif a == 0 or b == 0 or c == 0:
            print("Encendido.")
            print("Encendido.")
            print("Encendido.")
        else:
            print("Encendido.")
            print("Encendido.")
            print("Encendido.")

    except ValueError:
        print("No hay un numero.")     