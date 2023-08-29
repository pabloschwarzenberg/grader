def levenshtein(palabra1,palabra2) :
    palabra1 = list(palabra1)
    palabra2 = list(palabra2)
    if len(palabra1) > len(palabra2) :
        c = len(palabra1)
    if len(palabra2) > len(palabra1) :
        c = len(palabra2)
    for i in range(len(palabra1)):
        for j in range(len(palabra2)):
            if palabra1[i] == palabra2[j] :
                c -= 1
    if c > 1 :
        print("+1")
    elif c == 1 :
        if len(palabra1) == len(palabra2) :
            print("1S")
        elif len(palabra1) != len(palabra2) :
            print("IB")
    elif palabra1 == palabra2 :
        print("0D")