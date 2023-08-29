import random


def ocultar_letras(palabra, cantidad):
    conta = -1
    secre = []
    juan = []
    pal = ""
    jamon = 0
    for l in palabra:
        conta += 1
        secre.append(l)
        juan.append(int(conta))
    letra = random.sample(juan, cantidad)
    for p in range(cantidad):
        secre[letra[jamon]] = "_"
        jamon += 1

    for j in secre:
        pal += j
    palabra = pal
    return palabra


def revisar_letra(palabra_secreta, palabra, letra):
    mis = []
    mas = []
    largo = -1
    real = 0
    resutado = ""
    for k in palabra:
        mis.append(k)
        real += 1
    for g in palabra_secreta:
        mas.append(g)
    for h in range(real):
        largo += 1
        if letra == mas[largo] and mis[largo] == "_":
            mis[largo] = letra
    for j in mis:
        resutado += j
    palabra = resutado
    palabra_secreta = resutado
    return palabra


if __name__ == "__main__":
    a = ["lepidoptero"]
    b = int(input())
    c = ocultar_letras(a[0], b)
    print(c)
    for ñ in range(7):
        d = input()
        c = revisar_letra(a, c, d)
        print(c)
    pass