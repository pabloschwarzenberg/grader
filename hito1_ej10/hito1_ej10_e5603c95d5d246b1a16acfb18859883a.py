class Cajero:
    def __init__(self):
        self.saldo_cajero = 1000000
    
    def ingresar(self):
        usuario = "10334151"
        clave = "1803"
        saldo_cuenta = 100000
        intentos = 0
        
        while intentos < 3:
            input_usuario = input("Ingrese el usuario: ")
            input_clave = input("Ingrese la clave: ")
            
            if input_usuario == usuario and input_clave == clave:
                self.realizar_retiro(saldo_cuenta)
                break
            else:
                print("Clave inválida.")
                intentos += 1
                
        if intentos == 3:
            print("Tarjeta bloqueada.")
    
    def realizar_retiro(self, saldo_cuenta):
        monto = int(input("Ingrese el monto a retirar: "))
        
        if monto <= saldo_cuenta and monto <= self.saldo_cajero:
            saldo_cuenta -= monto
            self.saldo_cajero -= monto
            print("Retiro exitoso.")
            print("Saldo cuenta={}".format(saldo_cuenta))
            print("Saldo cajero={}".format(self.saldo_cajero))
        else:
            print("Monto no permitido.")
    
    def ejecutar_cajero(self):
        while True:
            self.ingresar()
            opcion = input("¿Desea realizar otra transacción? (S/N): ")
            
            if opcion.upper() != "S":
                break

cajero = Cajero()
cajero.ejecutar_cajero()
