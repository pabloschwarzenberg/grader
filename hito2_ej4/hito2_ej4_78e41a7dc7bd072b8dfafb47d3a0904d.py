# Carro de compras
# Autor: Felipe Gutierrez Lucero

# Productos
p1=[1,"Pokemon X",33.77]
p2=[2,"Nintendo XL",203]
p3=[3,"Mario Kart 7",27.58]
p4=[4,"PlayStation 4",348.00]
p5=[5,"FIFA 16",51.19]

carro=[]

def ver(entry):
    parsed=entry.split(',')
    a=int(parsed[0])
    b=int(parsed[1])
    # Agregar producto y cantidad del producto, al carro
    if a == 1:
        carro.append(p1[1])
        carro.append(b)
    elif a == 2:
        carro.append(p2[1])
        carro.append(b)
    elif a == 3:
        carro.append(p3[1])
        carro.append(b)
    elif a == 4:
        carro.append(p4[1])
        carro.append(b)
    elif a == 5:
        carro.append(p5[1])
        carro.append(b)

def checkout():
    # contadores de productos
    c_pokemon=0
    c_nintendo=0
    c_mariokart=0
    c_play4=0
    c_fifa16=0
    # 1. Recorrer el carro de compras
    conta_min=0
    conta_max=len(carro)
    while conta_min < conta_max:
        # para sacar la cantidad de producto
        index=conta_min+1
        cant=carro[index]
        if carro[conta_min] == "Pokemon X":
            c_pokemon+=cant
            cant=0
        elif carro[conta_min] == "Nintendo XL":
            c_nintendo+=cant
            cant=0
        elif carro[conta_min] == "Mario Kart 7":
            c_mariokart+=cant
            cant=0
        elif carro[conta_min] == "PlayStation 4":
            c_play4+=cant
            cant=0
        elif carro[conta_min] == "FIFA 16":
            c_fifa16+=cant
            cant=0
        conta_min=conta_min+2
    # 2. Calcular precios
    precio1=0
    precio2=0
    total=0
    # con descuento
    if c_pokemon >=1 and c_nintendo>=1 and c_mariokart>=1:
        dcto1=0.8
        precio1=(c_pokemon*p1[2]+c_nintendo*p2[2]+c_mariokart*p3[2])*dcto1
        total+=precio1
    if c_play4 >=1 and c_fifa16 >=1:
        dcto2=0.85
        precio2=(c_play4*p4[2]+c_fifa16*p5[2])*dcto2
        total+=precio2
    # sin descuento
    if (not (c_pokemon >=1 and c_nintendo>=1 and c_mariokart>=1)) and (not (c_play4 >=1 and c_fifa16 >=1)):
        total+=(c_pokemon*p1[2]+c_nintendo*p2[2]+c_mariokart*p3[2]+c_play4*p4[2]+c_fifa16*p5[2])
    # para imprimir el resultado redondeado a 1 decimal
    p_total=round(total,1)
    #print(carro)
    #print(p_total)
    return p_total

# Display productos
print("""Productos disponibles:
1 - "Pokemon X" ($33.77)
2 - "Nintendo XL" ($203)
3 - "Mario Kart 7" ($27.58)
4 - "PlayStation 4" ($348.00)
5 - "FIFA 16" ($51.19) """)
# Inputs
flag=True
entrada=input("Ingrese el numero del producto, junto a la cantidad que desea añadir: ")
ver(entrada)