class CarroDeCompras:
    def __init__(self):
        self.carro = []
    
    def agregar_producto(self, producto):
        self.carro.append(producto)
    
    def mostrar_carro(self):
        for producto in self.carro:
            print(producto)
    
    def calcular_descuento(self):
        descuento = 0
        
        # Descuento del 20% si se agregaron productos 1, 2 y 3 al carro
        if ("1" in self.carro) and ("2" in self.carro) and ("3" in self.carro):
            descuento = 0.2 * self.calcular_valor_total()
        
        # Descuento del 15% si se agregaron productos 4 y 5 al carro
        if ("4" in self.carro) and ("5" in self.carro):
            descuento = 0.15 * self.calcular_valor_total()
        
        return descuento
    
    def calcular_valor_despacho(self, tipo_despacho):
        valor_despacho = 0
        
        # Despacho aéreo normal: 20% del valor de los productos
        if tipo_despacho == 0:
            valor_despacho = 0.2 * self.calcular_valor_total()
        
        # Despacho aéreo express: 30% del valor de los productos
        elif tipo_despacho == 1:
            valor_despacho = 0.3 * self.calcular_valor_total()
        
        return valor_despacho
    
    def calcular_valor_total(self):
        valor_total = 0
        
        for producto in self.carro:
            valor_total += producto.precio
        
        return valor_total
    
    def checkout(self, tipo_despacho, direccion):
        descuento = self.calcular_descuento()
        valor_despacho = self.calcular_valor_despacho(tipo_despacho)
        
        if "chile" in direccion.lower():
            impuesto = 0.2 * (self.calcular_valor_total() - descuento + valor_despacho)
        else:
            impuesto = 0
        
        valor_total = self.calcular_valor_total() - descuento + valor_despacho + impuesto
        
        return valor_total
           