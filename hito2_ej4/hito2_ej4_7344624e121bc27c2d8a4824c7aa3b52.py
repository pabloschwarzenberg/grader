CC = 0
carro = []
while CC != -1:
    comando = input("Ingrese su orden: ")
    if len(comando) == 3:
        carro.append([comando[0],comando[2]])
    if comando == "ver":
        for x in carro:
            print(x)
    if comando == "checkout":
        C1 = 0
        C2 = 0
        C3 = 0
        C4 = 0
        C5 = 0
        A = ['1',',2','3']
        B = ['4','5']
        A1 = []
        B1 = []
        precio = 0
        for x in carro:
            print(x,x[0],x[1])
            if x[0] == '1':
                precio+=33.77*int(x[1])
                A1.append(x[0])
                C1+=1
            elif x[0] == '2':
                precio+=203*int(x[1])
                A1.append(x[0])
                C2+=1
            elif x[0] == '3':
                precio+=27.58*int(x[1])
                A1.append(x[0])
                C3+=1
            elif x[0] == '4':
                precio+=348*int(x[1])
                B1.append(x[0])
                C4+=1
            elif x[0] == '5':
                precio+=51.19*int(x[1])
                B1.append(x[0])
                C5+=1
        if C1>= 1 and C2>= 1 and C3>=1:
            precio-=0.2*precio
        if C4>= 1 and C5>= 1:
            precio-=0.15*precio
        precio = round(precio,1)
        print(precio)
        CC = -1     
      