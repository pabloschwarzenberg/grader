#Cajero Automático
 print("Programa Cajero ")
Saldo=0
Nro_Retiros=Nro_Depositos=0
while True:
    print("_________________________________________________")
    print("Que deseas hacer: 1...... Depositar")
    print("                  2...... Retirar")
    print("                  3...... Consultar Saldo ")
    print("_________________________________________________")
    Opcion_Menu=input("Tu Opcion: :")
    if Opcion_Menu =="1" or Opcion_Menu =="2" or Opcion_Menu =="3" :
        if Opcion_Menu=="1":
            Monto=float(input("Ingrese el monto ahorrar:"))
            Saldo+=Monto
            Nro_Depositos+=1
        if Opcion_Menu=="2":
            Monto=float(input("Ingrese el monto retirar:"))
            Saldo-=Monto # Acumulador
            Nro_Retiros+=1
        if Opcion_Menu=="3":
            print("Saldo de la cuenta: ",Saldo)
    else :
        print("Opcion incorrecta ")
    Respuesta=input("Deseas Seguir procesando operaciones bancarias (S/N):")
    if Respuesta=="N" or Respuesta=="n" : break
print("_________________________________________________")
print("Saldo Final de la Cta: ",Saldo)
print("Nro de operaciones de Depositos:",Nro_Depositos)
print("Nro de operaciones de Retiros:",Nro_Retiros)
print("_________________________________________________")
     