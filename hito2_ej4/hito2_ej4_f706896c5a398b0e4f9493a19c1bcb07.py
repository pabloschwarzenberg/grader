def comprar(producto,cantidad):
    item=[]
    P=float(producto)
    for i in range(len(utbud)):
        if P in utbud[i]:
            P=utbud[i]
            item.append(P)
    item.append(float(cantidad))
    carro.append(item)

def promociones(carro_c):
    n_20=0
    n_15=0
    i=0
    while i<len(carro_c):
        if carro_c[i][0][0]==1 or carro_c[i][0][0]==2 or carro_c[i][0][0]==3:
            n_20+=1
        elif carro_c[i][0][0]==4 or carro_c[i][0][0]==5:
            n_15+=1
        i+=1
    i=0
    while i<len(carro_c):
        if n_20==3:
            carro_c[i][0][2]*=0.8
        elif n_15==2:
            carro_c[i][0][2]*=0.85
        i+=1
    return carro_c

def valor(carro_c):
    v=0
    i=0
    for i in range(len(carro_c)):
        v+=carro_c[i][0][2]*carro_c[i][1]
    v=round(v,1)
    return v
                
if __name__ == "__main__":
    P1=[1, "Pokemon", 33.77]
    P2=[2, "Nintendo", 203]
    P3=[3, "Mario Kart", 27.58]
    P4=[4, "Playstation 4",348]
    P5=[5, "Fifa 16", 51.19]
    utbud=[P1,P2,P3,P4,P5]
    print(utbud)
    carro=[]

    o=""
    while o!="checkout" :       
        print("Menu")
        print("escribe ver:para ver el carro")
        print("Para agrergar algo en el carro ingrese primero numero de producto,cantidad")
        print("para hacer check-out, escribe: check-out")
        o=input("Ingrese opción: ")
        if o=="ver":
            print("Tu carro: ")
            print(carro)
        elif o[0].isdigit():    
            comprar(o[0],o[2])
            
    carro=promociones(carro)
    print("Tienes que pagar: "+ str(valor(carro)))