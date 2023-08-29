p1 = [1,"Pokemon X",33.77]
p2 = [2,"Nintendo XL",203]
p3 = [3,"Mario Kart 7",27.58]
p4 = [4,"PlayStation 4",348.00]
p5 = [5,"FIFA 16",51.19]

carrito = [0, 0, 0, 0, 0]

inst = ""
while inst != "checkout":
    inst = input()

    if ',' in inst:
        inst = inst.split(',')
        prod = int(inst[0])
        cant = int(inst[1])
        carrito[prod - 1] += cant
        
    elif inst == "ver":
        for n in range(len(carrito)):
            for i in range(carrito[n]):
                if n == 0:
                    print(p1)
                elif n == 1:
                    print(p2)
                elif n == 2:
                    print(p3)
                elif n == 3:
                    print(p4)
                elif n == 4:
                    print(p5)

precio = 0.0
done = False
while not done:
    if carrito[0] > 0 and carrito[1] > 0 and carrito[2] > 0:
        carrito[0] -= 1
        carrito[1] -= 1
        carrito[2] -= 1

        precio += (p1[2] + p2[2] + p3[2]) * 0.8
    elif carrito[3] > 0 and carrito[4]:
        carrito[3] -= 1
        carrito[4] -= 1

        precio += (p4[2] + p5[2]) * 0.85

    done = True

    for n in range(len(carrito)):
        for i in range(carrito[n]):
            if n == 0:
                precio += p1[2]
            elif n == 1:
                precio += p2[2]
            elif n == 2:
                precio += p3[2]
            elif n == 3:
                precio += p4[2]
            elif n == 4:
                precio += p5[2]

print(round(precio, 1))