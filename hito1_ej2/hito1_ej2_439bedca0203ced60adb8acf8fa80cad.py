n_T = int(input("Ingrese número telefónico: "))
h_L = int(input("Ingrese hora de llamada: "))

while True:
    if h_L >= 0 and h_L <= 7:
        print("CONTESTAR")

    if h_L < 14:
        if n_T % 1000 == 909:
            print("CONTESTAR")
            break

    if h_L >= 17 and h_L <= 19:
        if n_T // 1000 == 877:
            print("CONTESTAR")
            break

    if h_L >= 20:
        print("NO CONTESTAR")
        break
    else:
        h_L += 1
