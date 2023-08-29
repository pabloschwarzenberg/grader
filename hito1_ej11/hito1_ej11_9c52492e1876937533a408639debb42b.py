from time import sleep
s_cajero = 1000000
s_usuario = 100000
usuario = str(int(input("Ingrese Su Usuario")))
contraseña = str(int(input("Ingrese Su Contraseña")))
while True:
    if usuario == "10334151" and contraseña == "1803":
        print("Usuario y Contraseña Correctos")
        sleep(1)
        m_retiro = int(input("Ingrese El Monto Que Quiere Retirar"))
        if m_retiro>s_usuario and m_retiro>s_cajero:
            print("Monto No Permitido")
            break
        if m_retiro<s_usuario and m_retiro<s_cajero:
            s_usuario_f= s_usuario-m_retiro
            s_cajero_f = s_cajero-m_retiro
            print("Saldo Cuenta=",s_usuario_f)
            print("Saldo Cajero=",s_cajero_f)
            
            B_20m = int(m_retiro/20000)
            m_retiro = m_retiro%20000
            B_10m = int(m_retiro/10000)
            m_retiro = m_retiro%10000
            B_5m = int(m_retiro/5000)
            m_retiro = m_retiro%5000
            ##Billetes
            print("Billetes 20000=",B_20m)
            print("Billetes 10000=",B_10m)
            print("Billetes 5000=",B_5m)
        if m_retiro!="N":
            break