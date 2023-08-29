p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
          
class Carro:
    def __init__(self):
        carro = []
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.p5 = 0

    def agregar_producto(self, str):
        p, c = str.split(',')
        
        if p == '1':
            self.p1 += int(c)
        elif p == '2':
            self.p2 += int(c)
        elif p == '3':
            self.p3 += int(c)
        elif p == '4':
            self.p4 += int(c)
        elif p == '5':
            self.p5 += int(c)


    def ver(self):
        for i in range(5):
            print('{}: {}'.format([p1, p2, p3, p4, p5][i][1],
                                  [self.p1, self.p2, self.p3, self.p4, self.p5][i]))

    def checkout(self):
        precio = 0

        d1 = min(self.p1, self.p2, self.p3)
        d2 = min(self.p4, self.p5)

        precio += (1 - 0.20) * d1 * (p1[2] + p2[2] + p3[2])
        precio += (1 - 0.15) * d2 * (p4[2] + p5[2])

        precio += (self.p1 - d1) * p1[2]
        precio += (self.p2 - d1) * p2[2]
        precio += (self.p3 - d1) * p3[2]
        precio += (self.p4 - d2) * p4[2]
        precio += (self.p5 - d2) * p5[2]

        print(round(precio, 1))

if __name__ == '__main__':

    carro = Carro()
    op = 0

    while op != 'checkout':
        op = input()

        if op == 'ver':
            carro.ver()

        elif op == 'checkout':
            carro.checkout()

        else:
            if ',' in op:
                carro.agregar_producto(op)
            else:
                carro.agregar_producto(input())
