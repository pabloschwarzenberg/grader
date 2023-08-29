import analizador.util
import tema8_ej1.solucion
import tema8_ej1.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        tienda_r=tema8_ej1.solucion.Tienda()
        carro_r=tema8_ej1.solucion.Carro()
        carro_r.agregar_item(1,tienda_r.buscarProducto(1))
        carro_r.agregar_item(1,tienda_r.buscarProducto(2))
        carro_r.agregar_item(1,tienda_r.buscarProducto(3))
        total_normal_usa=carro_r.checkout(0,"usa")
        total_express_usa=carro_r.checkout(1,"usa")
        total_normal_chile=carro_r.checkout(0,"chile")
        total_express_chile=carro_r.checkout(1,"chile")

        tienda_i=self.modulo.Tienda()
        carro_i=self.modulo.Carro()
        carro_i.agregar_item(1,tienda_i.buscarProducto(1))
        carro_i.agregar_item(1,tienda_i.buscarProducto(2))
        carro_i.agregar_item(1,tienda_i.buscarProducto(3))
        total_normal_usa_i=carro_i.checkout(0,"usa")
        total_express_usa_i=carro_i.checkout(1,"usa")
        total_normal_chile_i=carro_i.checkout(0,"chile")
        total_express_chile_i=carro_i.checkout(1,"chile")

        if total_normal_usa!=total_normal_usa_i:
            self.errores.append("Al agregar los productos 1,2,3 con despacho {0} a dirección en {1} el total debiera ser {2}".format(
                0,"usa",total_normal_usa))

        if total_express_usa!=total_express_usa_i:
            self.errores.append("Al agregar los productos 1,2,3 con despacho {0} a dirección en {1} el total debiera ser {2}".format(
                1,"usa",total_express_usa))

        if total_normal_chile!=total_normal_chile_i:
            self.errores.append("Al agregar los productos 1,2,3 con despacho {0} a dirección en {1} el total debiera ser {2}".format(
                0,"chile",total_normal_chile))

        if total_express_usa!=total_express_usa_i:
            self.errores.append("Al agregar los productos 1,2,3 con despacho {0} a dirección en {1} el total debiera ser {2}".format(
                1,"chile",total_express_chile))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema8_ej1.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)