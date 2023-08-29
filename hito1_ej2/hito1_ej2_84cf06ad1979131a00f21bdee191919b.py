while(True):
    Telefono = int(input("Ingrese su numero de telefono: "))
    H_llamada = int(input("Ingrese la hora de la llamada: "))
    if 1000000000 <= Telefono or Telefono <= 9999999 or H_llamada > 23 or H_llamada < 0:
        print("Datos no validos")
    else:
        break
U_trescrifras = Telefono % 1000
P_cifras = Telefono // 100000
if 7 >= H_llamada >= 0:
    print("Contestar")
elif H_llamada >= 8 and H_llamada <= 14:
    if U_trescrifras == 909:
        print("Contestar")
    else:
        print("No contestar")
elif H_llamada >= 17 and H_llamada <= 19:
    if P_cifras == 877:
        print("No contestar")
    else:
        print("Contestar")
elif H_llamada >= 19:
    print("No contestar")