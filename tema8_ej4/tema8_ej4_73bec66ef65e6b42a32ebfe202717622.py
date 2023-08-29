def rot13(palabra):
    lista=[]
    for i in palabra:
        if i=="a":
            palabra=palabra.replace("a","n",len(palabra))
            i="n"
            lista.append(i)
        elif i=="b":
            i="o"
            palabra=palabra.replace("b","o",len(palabra))
            lista.append(i)
        elif i=="c":
            i="p"
            palabra=palabra.replace("c","p",len(palabra))
            lista.append(i)
        elif i=="d":
            i="q"
            palabra=palabra.replace("d","q",len(palabra))
            lista.append(i)
        elif i=="e":
            i="r"
            palabra=palabra.replace("e","r",len(palabra))
            lista.append(i)
        elif i=="f":
            i="s"
            palabra=palabra.replace("f","s",len(palabra))
            lista.append(i)
        elif i=="g":
            i="t"
            palabra=palabra.replace("g","t",len(palabra))
            lista.append(i)
        elif i=="h":
            i="u"
            palabra=palabra.replace("h","u",len(palabra))
            lista.append(i)
        elif i=="i":
            i="v"
            palabra=palabra.replace("i","v",len(palabra))
            lista.append(i)
        elif i=="j":
            i="w"
            palabra=palabra.replace("j","w",len(palabra))
            lista.append(i)
        elif i=="k":
            i="x"
            palabra=palabra.replace("k","x",len(palabra))
            lista.append(i)
        elif i=="l":
            i="y"
            palabra=palabra.replace("l","y",len(palabra))
            lista.append(i)
        elif i=="m":
            i="z"
            palabra=palabra.replace("m","z",len(palabra))
            lista.append(i)
        elif i=="n":
            i="a"
            palabra=palabra.replace("n","a",len(palabra))
            lista.append(i)
        elif i=="o":
            i="b"
            palabra=palabra.replace("o","b",len(palabra))
            lista.append(i)
        elif i=="p":
            i="c"
            palabra=palabra.replace("p","c",len(palabra))
            lista.append(i)
        elif i=="q":
            i="d"
            palabra=palabra.replace("q","d",len(palabra))
            lista.append(i)
        elif i=="r":
            i="e"
            palabra=palabra.replace("r","e",len(palabra))
            lista.append(i)
        elif i=="s":
            i="f"
            palabra=palabra.replace("s","f",len(palabra))
            lista.append(i)
        elif i=="t":
            i="g"
            palabra=palabra.replace("t","g",len(palabra))
            lista.append(i)
        elif i=="u":
            i="h"
            palabra=palabra.replace("u","h",len(palabra))
            lista.append(i)
        elif i=="v":
            i="i"
            palabra=palabra.replace("v","i",len(palabra))
            lista.append(i)
        elif i=="w":
            i="j"
            palabra=palabra.replace("w","j",len(palabra))
            lista.append(i)
        elif i=="x":
            i="k"
            palabra=palabra.replace("x","k",len(palabra))
            lista.append(i)
        elif i=="y":
            i="l"
            palabra=palabra.replace("y","l",len(palabra))
            lista.append(i)
        elif i=="z":
            i="m"
            palabra=palabra.replace("z","m",len(palabra))
            lista.append(i)
    return "".join(lista)