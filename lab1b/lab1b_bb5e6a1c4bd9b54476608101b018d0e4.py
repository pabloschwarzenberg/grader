#Heladas
temperatura=7
sensor_1=float(input("Ingrese temperatura 1: "))
sensor_2=float(input("Ingrese temperatura 2: "))
sensor_3=float(input("Ingrese temperatura 3: "))
while temperatura>5:
    if sensor_1<=0 or sensor_2<=0 or sensor_3<=0:
        print("Calefactores encendidos")
    else:
        if sensor_1>5:
            print("Calefactor 1 apagado")
        else:
            print("Calefactor 1 encendido")
        if sensor_2>5:
            print("Calefactor 2 apagado")
        else:
            print("Calefactor 2 encendido")
        if sensor_3>5:
            print("Calefactor 3 apagado")
        else:
            print("Calefactor 3 encendido")
    sensor_1=int(input("Ingrese temperatura 1: "))
    sensor_2=int(input("Ingrese temperatura 2: "))
    sensor_3=int(input("Ingrese temperatura 3: "))