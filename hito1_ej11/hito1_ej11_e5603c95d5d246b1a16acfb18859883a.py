class Cajero:
    def __init__(self):
        self.saldo_cajero = {
            20000: 20,
            10000: 40,
            5000: 40
        }
    
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
        
        if monto <= saldo_cuenta and monto <= self.calcular_saldo_total():
            billetes_entregados = self.distribuir_billetes(monto)
            
            if billetes_entregados:
                saldo_cuenta -= monto
                print("Retiro exitoso.")
                print("Saldo cuenta={}".format(saldo_cuenta))
                self.imprimir_billetes_entregados(billetes_entregados)
                self.actualizar_saldo_cajero(billetes_entregados)
                print("Saldo cajero={}".format(self.calcular_saldo_total()))
            else:
                print("No hay suficientes billetes para realizar el retiro.")
        else:
            print("Monto no permitido.")
    
    def distribuir_billetes(self, monto):
        billetes_entregados = {
            20000: 0,
            10000: 0,
            5000: 0
        }
        
        for denominacion in self.saldo_cajero.keys():
            cantidad_disponible = self.saldo_cajero[denominacion]
            cantidad_billetes = min(monto // denominacion, cantidad_disponible)
            billetes_entregados[denominacion] = cantidad_billetes
            monto -= cantidad_billetes * denominacion
            
        if monto == 0:
            return billetes_entregados
        else:
            return None
    
    def imprimir_billetes_entregados(self, billetes_entregados):
        for denominacion, cantidad in billetes_entregados.items():
            if cantidad > 0:
                print("billetes {}={}".format(denominacion, cantidad))
    
    def actualizar_saldo_cajero(self, billetes_entregados):
        for denominacion, cantidad in billetes_entregados.items():
            self.saldo_cajero[denominacion] -= cantidad
    
    def calcular_saldo_total(self):
        return sum(denominacion * cantidad for denominacion, cantidad in self.saldo_cajero.items())
    
    def ejecutar_cajero(self):
        while True:
            self.ingresar()
            opcion = input("¿Desea realizar otra transacción? (S/N): ")
            
            if opcion.upper() != "S":
                break

cajero = Cajero()
cajero.ejecutar_cajero()
