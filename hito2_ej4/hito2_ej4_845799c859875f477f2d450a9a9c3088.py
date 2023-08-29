print("""   
a - AGREGAR PRODUCTOS AL CARRO
ver - MOSTRARLOS 
checkout - HACER EL CHECKOUT
""")

op = str(input("SELECCIONE UNA OPCIÓN: "))

carro = []
s1=0
s2=0
s3=0
s4=0
s5=0

totalgeneral=0

if op == "a":
    print("""
1 - Juego Pokemon X para Nintendo 3DS, USD 33.77
2 - Nintendo 3DS XL, USD 203
3 - Juego Mario Kart 7 para Nintendo 3DS, USD 27.58
4 - PlayStation 4, USD 348.00
5 - FIFA 16, PlayStation 4, USD 51.19
0,0 - salir
""")
    while True:
        selp = str(input("SELECCIONE producto,cantidad: "))
        prod = selp[0]
        cantp = selp[2]
        if prod == 1:
            s1+=1
            tdp1 = cantp * 33.77
            totalgeneral+=tdp1
            carro.append("Juego Pokemon X para Nintendo 3DS, USD 33.77 - Unidades:",cantp, "Total:",tdp1)
        elif prod == 2:
            s2+=1
            tdp2 = cantp * 203
            totalgeneral+=tdp2
            carro.append("Nintendo 3DS XL, USD 203 - Unidades:",cantp, "Total:",tdp2)
        elif prod == 3:
            s3+=1
            tdp3 = cantp * 27.58
            totalgeneral+=tdp3
            carro.append("Juego Mario Kart 7 para Nintendo 3DS, USD 27.58 - Unidades:",cantp, "Total:",tdp3)
        elif prod == 4:
            s4+=1
            tdp4 = cantp * 348
            totalgeneral+=tdp4
            carro.append("PlayStation 4, USD 348.00 - Unidades:",cantp, "Total:",tdp4)
        elif prod == 5:
            s5+=1
            tdp5 = cantp * 51.19
            totalgeneral+=tdp5
            carro.append("FIFA 16, PlayStation 4, USD 51.19 - Unidades:",cantp, "Total:",tdp5)
        elif prod == 0 and cantp == 0:
            break
        
elif op == "ver":
    print(carro)  
elif op == "checkout":
    print(carro)
    if s1 > 0 and s2 > 0 and s3 > 0:
        totaal=totalgeneral*0.8
        print(totaal)
    elif s4 > 0 and s5 > 0:
        ttotal=totalgeneral*0.85
        print(ttotal)