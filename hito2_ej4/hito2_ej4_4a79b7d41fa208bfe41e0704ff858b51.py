# carro de compras

def ver(carro,productos):
    
    for i in range(len(productos)):
        print (str(productos[i][1])+": "+str(carro[i]))
        
    return 0

def checkout(carro,productos):
    
    ratio = 1
    ratio_a = 1
    ratio_b = 1
    
    if carro[0]>0 and carro[1]>0 and carro[2]>0:
        ratio_a = 0.80
    
    if carro[3] > 1 and carro[4] > 1:
        ratio_b = 0.85
    
    # encontrar el total del carro
    total = 0
    
    for i in range(len(carro)):
        total += carro[i]*productos[i][2]
    
    print("%.1f" % total)

# definicion de productos
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]
productos = [p1,p2,p3,p4,p5]
      
# carro de compras: empezamos la cantidad en 0
carro = [0]*5

# input para ingresar productos
while True:
    
    string = input("Ingrese un producto (1-5) y cantidad (e.g. 5,3), ver, o checkout: \t")
    
    if string == "ver":
        ver(carro,productos)
    elif string == "checkout":
        checkout(carro,productos)
        break
    else:
        producto = string[0]
        cantidad = string[2]
        carro[int(producto)-1] += int(cantidad)  
    