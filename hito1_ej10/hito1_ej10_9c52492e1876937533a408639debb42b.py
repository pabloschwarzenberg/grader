#Cajero Automático
from time import sleep
s_cajero = 1000000
s_usuario = 100000
usuario = str(int(input("Ingrese Su Usuario")))
contrasena = str(int(input("Ingrese Su Contraseña")))
while True:
    if usuario == "10334151" and contrasena == "1803":
        print("Usuario y Contraseña Son Correctos")
        sleep(1)
        m_retiro = int(input("Ingrese El Monto Que Quiere Retirar"))
        if m_retiro>s_usuario and m_retiro>s_cajero:
            print("Monto No Permitido")
            break
        if m_retiro<s_usuario and m_retiro<s_cajero:
            s_usuario_f = s_usuario-m_retiro
            s_cajero_f = s_cajero-m_retiro
            print("Saldo Cajero=", s_cajero_f)
            print("Saldo Cuenta=", s_usuario_f)
        if m_retiro!="N":
            break
    if usuario != "10334151" or contrasena != "1803":
        print("Clave Incorrecta")
        sleep(1)
        print("Segundo Intento")
        sleep(1)
        contrasena = str(int(input("Ingrese Nuevamente La Contraseña")))
        if usuario != "10334151" or contrasena != "1803":
            print("Clave Incorrecta")
            sleep(1)
            print("Tercer Intento")
            sleep(1)
            contrasena = str(int(input("Ingrese Nuevamente La Contraseña")))
            if usuario != "10334151" or contrasena != "1803":
                print("Se Ha Bloquedo La Tarjeta")
                break


            
            