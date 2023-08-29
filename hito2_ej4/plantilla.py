#esto es mejor definirlo fuera del ciclo porque no cambia
p1 = [1, "Pokemon X para Nintendo 3DS", 33.77]
p2 = [2, "Nintendo 3DS XL", 203]
p3 = [3, "Juego Mario Kart 7 para Nintendo 3DS", 27.58]
p4 = [4, "PlayStation 4", 348]
p5 = [5, "FIFA 16, PlayStation 4", 51.19]
ptos = [p1, p2, p3, p4, p5]

while True:

    kill = str(input("Ingrese accion: "))
    kill = kill.lower()

    if (kill != "ver" and kill != "checkout"):
        #es necesario llamar a la función split para separar en dos partes el texto
        #los productos se ingresan desde el 1 en adelante
        kill = kill.split(",")
        prod = int(kill[0])
        cant = int(kill[1])

    carro = []

    for x in range(cant):
        carro.append(ptos[prod])

    if (kill == "ver"):

        print(carro)

    elif (kill == "checkout"):

        z = carro.count(p1)
        e = carro.count(p2)
        f = carro.count(p3)
        r = carro.count(p4)
        qa = carro.count(p5)

        sec = z * p1[2]
        dec = e * p2[2]
        cec = f * p3[2]
        poc = r * p4[2]
        per = qa * p5[2]

        if sec > 0:

            sec = 0.8 * sec

        elif dec > 0:

            dec = 0.8 * dec

        elif cec > 0:

            cec = 0.8 * cec

        elif poc > 0:

            poc = 0.85 * poc

        elif per > 0:

            per = 0.85 * per

        noice = sec + cec + dec + per + poc
        noice = round(noice, 1)
        print(noice)

        break