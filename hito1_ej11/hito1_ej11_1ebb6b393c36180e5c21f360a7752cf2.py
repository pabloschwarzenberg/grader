#Cajero Automático
  print("_________________________________________________")
print("Programa Cajero - Cta:xxxxxxxx, Saldo yyyyyyy fecha: aaaammdd no mayor a 3 Millones")
print("Ejemplo de ráfaga - 270295702765678")
print("_________________________________________________")
rafaga=int(input("Introduzca la rafaga:"))
Saldo=rafaga % 10000000 #correr izq-derecho, módulo   787878578
Rut_Cta=rafaga // 10000000 #correr lado derecha-izquierdo, división entera
Nro_Retiros=Nro_Depositos=0
Tope_Ahorro=3000000
while True:
    print("Cajero operando con el cliente: "+ str(Rut_Cta)+" Saldo :"+str(Saldo))
    print("_________________________________________________")
    print("Que deseas hacer: 1...... Depositar")
    print("                  2...... Retirar")
    print("                  3...... Consultar Saldo ")
    print("_________________________________________________")
    Opcion_Menu=input("Tu Opcion: :")
    if Opcion_Menu =="1" or Opcion_Menu =="2" or Opcion_Menu =="3" :
        if Opcion_Menu=="1": # Depositar
            Monto=float(input("Ingrese el monto ahorrar:"))
            if Monto+Saldo <= Tope_Ahorro :
                Saldo+=Monto
                Nro_Depositos+=1
            else :
                print("Excede monto máximo ahorros")
        if Opcion_Menu=="2": # retirar
            Monto=float(input("Ingrese el monto retirar:"))
            if Monto <= Saldo-300 :
                Saldo-=Monto # Acumulador
                Nro_Retiros+=1
            else :
                print(" Saldo insuficiente")
        if Opcion_Menu=="3": # Consultar
            print("Saldo de la cuenta: ",Saldo)
    else :
        print(" Opcion no existente")
    Respuesta=input("Deseas Seguir procesando operaciones bancarias (S/N):")
    if Respuesta=="N" or Respuesta=="n" : break
print("_________________________________________________")
print("Saldo Final de la Cta: ",Saldo)
print("Nro de operaciones de Depositos:",Nro_Depositos)
print("Nro de operaciones de Retiros:",Nro_Retiros)
print("_________________________________________________")    