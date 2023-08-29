#Cajero Automático
saldo_de_caja = 1000000
saldo_usuario = 100000
usuario = str(int(input("Ingrese el usuario: ")))
clave = str(int(input("Ingrese la contraseña: ")))
while True: #mientras sea verdad
    if usuario == "10334151" and clave == "1803": #si el usuario es ... y la contraseña es ...
        print("Usuario y contraseña correctos")
        monto_a_retirar = int(input("Ingrese el monto a retirar: ")) #monto que desea retirar
        if monto_a_retirar>saldo_usuario and monto_a_retirar>saldo_de_caja: #si el monto a retirar es mayor saldo de usuario y el monto retirado es mayor a el saldo de la caja no permitir el retiro
            print("monto no permitido")
            break
        if monto_a_retirar<saldo_usuario and monto_a_retirar<saldo_de_caja:# si el monto es menor a el saldo del usuario  y  el monto a retirar es menor a el saldo de la caja puede sacar dinero
            saldo_usuario_final = saldo_usuario-monto_a_retirar #calculo 1
            saldo_cajero_final = saldo_de_caja-monto_a_retirar #calculo2
            print("saldo cuenta=", saldo_usuario_final)
            print("saldo cajero=", saldo_cajero_final)
            ##Billetes*
            billetes20k = int(monto_a_retirar/20000) #si retira billetes de 20k se divide y da el numero de billetes a retirar
            monto_a_retirar = monto_a_retirar%20000 
            billetes10k = int(monto_a_retirar/10000)
            monto_a_retirar = monto_a_retirar%10000
            billetes5k = int(monto_a_retirar/5000)
            monto_a_retirar = monto_a_retirar%5000
            ##Billetes
            print("billetes 20000= ", billetes20k)
            print("billetes 10000= ", billetes10k)
            print("billetes 5000= ", billetes5k)
        if monto_a_retirar!="N":
            break 