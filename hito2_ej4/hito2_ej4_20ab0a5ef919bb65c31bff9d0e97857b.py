class Amazon:
    def __init__(self):
        self.a=[ 
           [1,"Pokemon X     ",33.77] ,
           [2,"Nintendo XL   ",  203] ,
           [3,"Mario Kart 7  ",27.58] ,
           [4,"PlayStation 4 ",348.00] ,
           [5,"FIFA 16       ", 51.19] 
          ]
        
        self.carro=[]
        
    def mostrar_productos(self):
        for i in self.a:
            print( str(i[0]) + "  " + i[1] + " "*3 + str(i[2]) + " USD")

    def comprar(self,producto,cantidad):
        precio=self.a[producto-1][2]
        self.carro.append([producto,cantidad,precio])

    def mostrar_carro(self):
        return self.carro
    
    def checkout(self):
        pago=0
        veinte=0
        quince=0
        pago_final=0
        for i in self.carro:
            if(i[0]==1 or i[0]==2 or i[0]==3):
                veinte=veinte+20
            else:
                if(i[0]==4 or i[0]==5):
                    quince=quince+15
            pago=pago+(i[2]*i[1])
 
        if(veinte==60):
            veinte=veinte/3
            pago_final=pago-(pago*(veinte/100))
        else:
            if(quince==30):
                quince=quince/2
                pago_final=pago-(pago*(quince/100))
            else:
                pago_final=pago

        return (round(pago_final,1))        

App=Amazon()
precio_final=0
while True:
    entrada=input("Ingresar PRODUCTO,CANTIDAD o VER para ver productos o CHECKOUT para ver total : ")
    if(entrada=="checkout"):
        precio_final=App.checkout()
        print(precio_final)
        break
    else:
        if(entrada=="ver"):
            App.mostrar_productos()
        else:
            Producto = int(entrada[0])
            Cantidad = int(entrada[2])
            App.comprar(Producto,Cantidad)