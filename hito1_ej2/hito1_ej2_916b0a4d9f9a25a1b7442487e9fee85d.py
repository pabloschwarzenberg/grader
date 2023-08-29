print("Contestador de Celular")
numero=str(input("Ingrese número telefónico:"))
hora=int(input("Ingrese hora del día:"))
if hora>=0 and hora<=7:
    print("Resultado: CONTESTAR")
elif hora>7 and hora<14:
    if numero[5]=="9" and numero[6]=="0" and numero[7]=="9":
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora>=17 and hora<=19:
    if numero[0]!="8" and numero[1]!="7" and numero[2]!="7":
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")