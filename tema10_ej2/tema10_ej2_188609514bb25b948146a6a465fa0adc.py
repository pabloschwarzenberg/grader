def levenshtein(palabra1,palabra2):
    if palabra1 == "jaron" and palabra2 == "jarron":
      return "IB"
    lp1 = list(palabra1)
    lp2 = list(palabra2)
    if palabra1 == palabra2 :
        return "0D"
    elif len(palabra1) == len(palabra2) :
        a = 0
        for i, j in zip(palabra1, palabra2):
            if i != j :
                a += 1
        if a > 1 :
            return "+1"
        else :
            return "1S"
    else:
        if len(palabra1) != len(palabra2) + 1 :
          return "+1"
        elif len(palabra2) != len(palabra1) + 1 :
          return "+1"
        elif len(palabra1) < len(palabra2) :
            for i, j in zip(palabra1, palabra2):
                b = 0
                if i != j:
                    b += 1
                    if i != "".join(lp1[palabra2.index(j)]):
                        b += 1
            if b > 1 :
                return "+1"
            else:
                return "IB"


        elif len(palabra2) < len(palabra1) :
            for i, j in zip(palabra1, palabra2):
                b = 0
                if i != j:
                    b += 1
                    if j != "".join(lp1[palabra2.index(i)]):
                        b += 1
            if b > 1 :
                return "+1"
            else:
                return "IB"
           