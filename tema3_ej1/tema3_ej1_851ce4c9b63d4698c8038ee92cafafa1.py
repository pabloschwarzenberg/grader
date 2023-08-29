def suma_divisores(a):
    div = []
    for i in range(1, a+1):
        if a%i == 0:
            if i != a:
                div.append(i)
            else:
                continue
    suma = sum(div)
    esp = True
    if suma == 1:
        esp = True
    else:
        esp = False
    return suma,esp