#Contestador de celular
NroTel = int(input("Ingrese número telefónico: "))
HraLlamada = int(input("Ingrese hora de la llamada (formato 24 horas): "))

if HraLlamada >= 0 and HraLlamada <= 13:
    print("CONTESTAR")
elif HraLlamada < 13 and NroTel % 100 == 909:
    print("CONTESTAR")
elif HraLlamada >= 17 and HraLlamada <= 19 and NroTel // 10000000 == 877:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
