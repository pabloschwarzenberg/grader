def levenshtein(palabra1,palabra2):
    dif = len(palabra1) - len(palabra2)

    L1 = []
    L2 = []
    
    for x in palabra1:
        L1.append(x)

    for b in palabra2:
        L2.append(b)

    pa1 = L1[0:]
    pa2 = L2[0:]
     
    
    if palabra1 == palabra2:
        print("0D")
    elif pa1 != pa2:
        print("+1")
    elif pa1 != pa2 or dif != 0:
        print("IB")
    elif pa1 != pa2 or dif == 0:
        print("1S")
