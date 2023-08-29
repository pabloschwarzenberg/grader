sec = input("Ingresa una secuencia: ").strip()
n = int(input("ingresa largo de subsecuencia: "))
n=3
i = 0
encontro = False
while i < len(sec)-n+1:
    sub = sec[i:i+n]
    j = 0
    cont = 0
    while j < len(sec)-n+1:
        sub2 = sec[j:j+n]
        if sub == sub2:
            cont += 1
        j +=1
    if cont == 1:
        print(sub)
        encontro = True
    i = i+1
if not encontro:
    print('ninguna')