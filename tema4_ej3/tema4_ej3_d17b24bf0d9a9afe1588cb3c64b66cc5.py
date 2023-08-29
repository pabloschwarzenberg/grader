def jerigonzo(palabra):
    pal = []
    for i in palabra[0:]:
        if i == "a":
            pal.append(i + "p" + i)
        elif i == "e":
            pal.append(i + "p" + i)
        elif i == "i":
            pal.append(i + "p" + i)
        elif i == "o":
            pal.append(i + "p"+ i)
        elif i == "u":
            pal.append(i + "p"+ i)
        else:
            pal.append(i)

    palabra2= "".join(pal)
    return (palabra2)