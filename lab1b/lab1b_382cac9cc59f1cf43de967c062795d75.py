s1=float(input("Sensor 1: "))
s2=float(input("Sensor 2: "))
s3=float(input("Sensor 3: "))

if s1 <= 0 or s2<=0 or s3<=0:
    print("encendido")
    print("encendido")
    print("encendido")
else:
    if s1 <= 5:
        print("encendido")
    else:
        print("apagado")
    if s2 <= 5:
        print("encendido")
    else:
        print("apagado")
    if s3 <= 5:
        print("encendido")
    else:
        print("apagado")