def tiene_descuento1():
    try:
        if comprobar.index(1)!=-1 and comprobar.index(2)!=-1 and comprobar.index(3)!=-1:
            return True
    except:
        return False

def tiene_descuento2():
    try:
        if comprobar.index(4)!=-1 and comprobar.index(5)!=-1:
            return True
    except:
        return False

p1 = [1, "Pokemon X", 33.77]
p2 = [2, "Nintendo XL", 203]
p3 = [3, "Mario Kart 7", 27.58]
p4 = [4, "PlayStation 4", 348.00]
p5 = [5, "FIFA 16", 51.19]

comprados=[]
comprobar=[]
descuento=0

while True:
    print("Bienvenido que desea hacer")
    respuesta=input(">>>")
    if respuesta=="ver":
        print("Lista de productos:")
        print(p1)
        print(p2)
        print(p3)
        print(p4)
        print(p5)
    
    
    
    elif respuesta=="checkout":
        #print(comprados)
        for cada in comprados:
            comprobar.append(cada[0])
    
        if tiene_descuento1()==True:
            #print("Tiene descuento del 20% añadido")
            descuento=descuento+20
    
        if tiene_descuento2()==True:
            #print("Se añade 15% más de descuento")
            descuento+=15
    
    
        #print("Descuento total=%s "%descuento)
        sumatotal=0
        for cada in comprados:
            sumatotal+=cada[2]
        m=100-descuento
        sumatotal=sumatotal*m/100
    
        sumatotal=round(sumatotal,1)
        print(sumatotal)
        break
    
    
    else:
        respuesta=respuesta.split(",")
        cuantos=int(respuesta[1])
        if respuesta[0]=="1":
            for x in range(cuantos):
                comprados.append(p1)
        elif respuesta[0]=="2":
            for x in range(cuantos):
                 comprados.append(p2)
        elif respuesta[0]=="3":
            for x in range(cuantos):
                comprados.append(p3)
        elif respuesta[0]=="4":
            for x in range(cuantos):
                comprados.append(p4)
        elif respuesta[0]=="5":
            for x in range(cuantos):
                comprados.append(p5)