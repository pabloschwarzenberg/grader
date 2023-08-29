def adn(x):
    y = x.upper()
    genoma = ["A", "C", "T", "G"] * 1000
    import random
    random.shuffle(genoma)
    b = "".join(genoma)
    z = b.find(str(y))
    if z != -1:
        print("La secuencia", str(x), "es correcta")
    else:
        print("La secuencia", str(x), "es incorrecta")