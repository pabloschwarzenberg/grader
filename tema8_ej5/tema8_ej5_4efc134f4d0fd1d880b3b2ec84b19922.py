class FechaHora:
    def __init__(self, fecha=None, hora=None):
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"{self.fecha} {self.hora}"

    def fijarFecha(self, fecha):
        self.fecha = fecha

    def fijarHora(self, hora):
        self.hora = hora

    def fijarFechaHora(self, fechahora):
        fechahora = fechahora.split()
        self.fecha = fechahora[0]
        self.hora = fechahora[1]

    def cambiar(self, parte):
        partes = parte.split('=')
        if len(partes) != 2:
            print("Formato incorrecto. Debe ser 'nombre=valor'.")
            return
        nombre = partes[0].strip().lower()
        valor = partes[1].strip()
        if nombre == 'dd':
            if not self.validar_dia(int(valor)):
                print("Día inválido.")
                return
            self.fecha = self.actualizar_fecha('dia', int(valor))
        elif nombre == 'mm':
            if not self.validar_mes(int(valor)):
                print("Mes inválido.")
                return
            self.fecha = self.actualizar_fecha('mes', int(valor))
        elif nombre == 'aaaa':
            if not self.validar_anio(int(valor)):
                print("Año inválido.")
                return
            self.fecha = self.actualizar_fecha('anio', int(valor))
        elif nombre == 'hh':
            if not self.validar_hora(int(valor)):
                print("Hora inválida.")
                return
            self.hora = self.actualizar_hora('hora', int(valor))
        elif nombre == 'min':
            if not self.validar_minuto(int(valor)):
                print("Minuto inválido.")
                return
            self.hora = self.actualizar_hora('minuto', int(valor))
        elif nombre == 'ss':
            if not self.validar_segundo(int(valor)):
                print("Segundo inválido.")
                return
            self.hora = self.actualizar_hora('segundo', int(valor))
        else:
            print("Nombre de parámetro inválido.")

    def validar_dia(self, dia):
        return 1 <= dia <= 31

    def validar_mes(self, mes):
        return 1 <= mes <= 12

    def validar_anio(self, anio):
        return anio >= 0

    def validar_hora(self, hora):
        return 0 <= hora <= 23

    def validar_minuto(self, minuto):
        return 0 <= minuto <= 59

    def validar_segundo(self, segundo):
        return 0 <= segundo <= 59

    def actualizar_fecha(self, parte, valor):
        dia, mes, anio = map(int, self.fecha.split('/'))
        if parte == 'dia':
            dia = valor
        elif parte == 'mes':
            mes = valor
        elif parte == 'anio':
            anio = valor
        return f"{anio:04d}/{mes:02d}/{dia:02d}"

    def actualizar_hora(self, parte, valor):
        hora, minuto, segundo = map(int, self.hora.split(':'))
        if parte == 'hora':
            hora = valor
        elif parte == 'minuto':
            minuto = valor
        elif parte == 'segundo':
            segundo = valor
        return f"{hora:02d}:{minuto:02d}:{segundo:02d}"


class Producto:
    def __init__(self, codigo, nombre, stock, precio):
        self.codigo = codigo
        self.stock = stock
        self.precio = precio
        self.nombre = nombre

    def __eq__(self, other):
        if self.codigo == other.codigo:
            return True
        else:
            return False


class Item:
    def __init__(self, cantidad, producto):
        self.cantidad = cantidad
        self.producto = producto


class Carro:
    def __init__(self):
        self.lista_de_productos = []
        self.descuento = 0
        self.total = 0
        self.direccion = ""

    def agregar_item(self, cantidad, producto):
        for item in self.lista_de_productos:
            if item.producto == producto:
                if cantidad == 0:
                    self.lista_de_productos.remove(item)
                else:
                    item.cantidad = cantidad
                return
        item = Item(cantidad, producto)
        self.lista_de_productos.append(item)

    def checkout(self, tipoDespacho, direccion):
        descuentos = sum(item.cantidad * item.producto.precio for item in self.lista_de_productos) * self.descuento
        despacho = sum(item.cantidad * item.producto.precio for item in self.lista_de_productos) * (0.2 if direccion.lower().endswith("chile") else 0)
        total = sum(item.cantidad * item.producto.precio for item in self.lista_de_productos) - descuentos + despacho
        if tipoDespacho == 0:
            despacho += sum(item.cantidad * item.producto.precio for item in self.lista_de_productos) * 0.2
        elif tipoDespacho == 1:
            despacho += sum(item.cantidad * item.producto.precio for item in self.lista_de_productos) * 0.3
        return total + despacho

    def __repr__(self):
        s = "Carro de Compras:\n"
        for item in self.lista_de_productos:
            s = s + "{0}: {1}\n".format(item.cantidad, item.producto.nombre)
        return s


class Tienda:
    def __init__(self):
        self.catalogo = []
        producto = Producto(1, "Juego Pokemon Y", 10, 31.51)
        self.catalogo.append(producto)
        producto = Producto(2, "Nintendo 3DS", 5, 190.95)
        self.catalogo.append(producto)
        producto = Producto(3, "Juego Mario Kart", 10, 29.96)
        self.catalogo.append(producto)
        producto = Producto(4, "Playstation 4", 10, 399)
        self.catalogo.append(producto)
        producto = Producto(5, "Fifa 14", 10, 41.95)
        self.catalogo.append(producto)

    def menu(self):
        for producto in self.catalogo:
            print("{0}: {1} ${2}".format(
                producto.codigo, producto.nombre, producto.precio))

    def buscarProducto(self, numero):
        for producto in self.catalogo:
            if producto.codigo == numero:
                return producto


if __name__ == "__main__":
    tienda = Tienda()
    carro = Carro()
    while True:
        tienda.menu()
        item_ingresado = input("Ingresa un producto a comprar (numero,cantidad): ")
        if item_ingresado == "checkout":
            tipoDespacho = int(input("Ingresa el tipo de despacho (0 - Aéreo Normal, 1 - Aéreo Express): "))
            direccion = input("Ingresa la dirección de despacho: ")
            total_pagar = carro.checkout(tipoDespacho, direccion)
            print("El total a pagar es: ${:.2f}".format(total_pagar))
            break
        elif item_ingresado == "":
            continue
        else:
            numero, cantidad = map(int, item_ingresado.split(","))
            producto = tienda.buscarProducto(numero)
            carro.agregar_item(cantidad, producto)

