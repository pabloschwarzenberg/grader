class Producto:
    def __init__(self,codigo,nombre,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.descuento=0

    def __str__(self):
        return "codigo = "+str(self.codigo)+" "+self.nombre+" con precio= "+str(self.precio)
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self,other):
        if self.codigo==other.codigo:
            return True
        else:
            return False

    def precio_promocion(self):
        return self.precio-self.precio*self.descuento
p1=Producto(1,"Pokemon X",33.77)
p2=Producto(2,"Nintendo XL",203)
p3=Producto(3,"Mario Kart 7",27.58)
p4=Producto(4,"PlayStation 4",348.00)
p5=Producto(5,"FIFA 16",51.19)
      