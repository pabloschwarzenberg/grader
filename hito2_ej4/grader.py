import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        self.p1 = [1, "Pokemon X", 33.77]
        self.p2 = [2, "Nintendo XL", 203]
        self.p3 = [3, "Mario Kart 7", 27.58]
        self.p4 = [4, "PlayStation 4", 348.00]
        self.p5 = [5, "FIFA 16", 51.19]

        analizador.util.AnalizadorBase.__init__(self)
        self.productos = [self.p1, self.p2, self.p3, self.p4, self.p5]
        self.carro=[]
        o1=random.choice(self.productos)
        i=self.productos.index(o1)
        self.productos.pop(i)
        q1=random.randint(1,3)
        o2=random.choice(self.productos)
        i=self.productos.index(o2)
        self.productos.pop(i)
        q2=random.randint(1,3)
        o3=random.choice(self.productos)
        i=self.productos.index(o3)
        self.productos.pop(i)
        q3=random.randint(1,3)
        self.carro=[[o1,q1],[o2,q2],[o3,q3]]
        precio=round(self.checkout(self.carro),1)
        self.setup=[[
            ",".join([str(o1[0]),str(q1)]),
            ",".join([str(o2[0]),str(q2)]),
            ",".join([str(o3[0]),str(q3)]),
        "checkout"]]
        self.output=[[str(precio)]]
        self.precondiciones=[self.setup_caso1]
        self.revisiones=[self.caso1]

    def checkout(self,carro):
        descuento = 0
        compras = []
        valor = 0
        for item in carro:
            compras.append(item[0])
            valor = valor + item[0][2] * item[1]
        if self.p1 in compras and self.p2 in compras and self.p3 in compras:
            descuento += 0.2
        if self.p4 in compras and self.p5 in compras:
            descuento += 0.15
        precio = valor - valor * descuento
        return precio

    def setup_caso(self,i):
        sys.stdin=io.StringIO()
        for dato in self.setup[i]:
            sys.stdin.write("{0}\n".format(dato))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def revisar_caso(self,i):
        salida=sys.stdout.getvalue().strip().lower().replace(" ","")
        for patron in self.output[i]:
            if salida.find(patron)==-1:
                self.errores.append("Para la compra: {0} el valor esperado es {1}".format(
                    self.setup[i],self.output[i][0]))
                return

    def setup_caso1(self):
        self.setup_caso(0)

    def caso1(self):
        self.revisar_caso(0)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","plantilla.py")
    for error in analizador.errores:
        print(error)