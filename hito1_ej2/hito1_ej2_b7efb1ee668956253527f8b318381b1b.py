#Contestador de celular
NT = int(input("Ingrese numero telefonico: "))
HLL = int(input("Ingrese hora de la llamada: "))
c2 = NT/1000
c2 = round(c2, 0)
con2 = NT-c2*1000
con2 = int(con2)
c3 = NT/100000
c3 = int(c3)
while NT<10000000:
          print("Numero invalido")
          NT = int(input("Ingrese numero telefonico: "))
else:
    if 0<=HLL<=7:
          print("Resultado: CONTESTAR")
    elif 7<HLL and HLL<14:
        if con2<909 and con2>909:
            print("Resultado: NO CONTESTAR")
        else:
            print("Resultado: CONTESTAR")
    elif 14<=HLL<17:
        print("Resultado: CONTESTAR")
    elif 17<=HLL<=19:
        if c3<877 and c3>877:
            print("Resultado: CONTESTAR")
        else:
            print("Resultado: NO CONTESTAR")
    elif HLL>19:
        print("Resultado: NO CONTESTAR")