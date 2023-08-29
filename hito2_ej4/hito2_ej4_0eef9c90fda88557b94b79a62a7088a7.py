
compra2 = []
compra = []
costo = 0
contador = 0
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

f1 = False
f2 = False
f3 = False
f4 = False
f5 = False

string = ""
while True:
    x = input("ingresa tu producto y la cantidad: ")
    compra.append(x)
    if "ver" in compra:
        compra.remove("ver")
        print(compra)
        
    if "checkout" in compra:
        break
for n in compra:
    n = n.replace(",", ".")
    compra2.append(n)
print(compra2)
while contador < len(compra)-1:
    if int(float(compra2[contador])) == 1:
        f1 = True
        cantidad = float(compra2[contador])
        costo += p1[2] * int(round(abs(cantidad) - abs(int(cantidad)), 1)*10)
        
    elif int(float(compra2[contador])) == 2:
        f2 = True
        cantidad = float(compra2[contador])
        costo += p2[2] *int(round(abs(cantidad) - abs(int(cantidad)), 1)*10)
    elif int(float(compra2[contador])) == 3:
        f3 = True
        cantidad = float(compra2[contador])
        costo += p3[2] *int(round(abs(cantidad) - abs(int(cantidad)), 1)*10)
    elif int(float(compra2[contador])) == 4:
        f4 = True
        cantidad = float(compra2[contador])
        costo += p4[2] *int(round(abs(cantidad) - abs(int(cantidad)), 1)*10)
    elif int(float(compra2[contador])) == 5:
        f5 = True
        cantidad = float(compra2[contador])
        costo += p5[2] *int(round(abs(cantidad) - abs(int(cantidad)), 1)*10)
    contador += 1
print(costo)
if f1 == True and f2 == True and f3 == True:
    costo = costo - (costo *0.2)
if f4 == True and f5 == True:
    costo = costo - (costo*0.15)
print(round(costo,1))