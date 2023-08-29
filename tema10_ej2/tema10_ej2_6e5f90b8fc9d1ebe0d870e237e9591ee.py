#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
import copy 
def levenshtein(a,b):
    if len(a) +2 >= len(b):
        return "+1"
    if len(b)+2 >= len(b):
        return "+1"
    if len(b)+1== len(a):
        for i in range (0,len(b)):
            b1=b.copy()
            b1.pop(i)
            if b1==a:
                return "IB"
        for i in range(0,len(a)):
            a1=a.copy
            a1.insert(i,"a")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "b")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "c")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "d")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.pop(i)
            a1.insert(i, "e")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "f")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "g")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "h")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "i")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "j")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "k")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "l")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "m")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "n")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "ñ")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "o")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "p")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "q")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "r")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "s")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "t")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "u")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "u")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "v")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "w")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "x")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "y")
            if a1 == b:
                return "IB"
            a1.pop(i)
            a1.insert(i, "z")
            if a1 == b:
                return "IB"
        return "+1"

    if len(a)+1== len(b):
        for i in range (0,len(b)):
            a1=b.copy()
            a1.pop(i)
            b=a
            if a1==b:
                return "IB"
        for i in range(0, len(a)):
            a1 = a.copy
            a1.insert(i, "a")
           





    if len(a)==len(b):
        if a== b:
            return "0D"
        elif a!=b:
            a=list(a)
            b=list(b)
            for i in range(0,len(a)):
                a[i]=="a"
                if a==b:
                    return "1S"
                a[i] == "b"
                if a == b:
                    return "1S"
                a[i] == "c"
                if a == b:
                    return "1S"
                a[i] == "d"
                if a == b:
                    return "1S"
                a[i] == "e"
                if a == b:
                    return "1S"
                a[i] == "f"
                if a == b:
                    return "1S"
                a[i] == "g"
                if a == b:
                    return "1S"
                a[i] == "h"
                if a == b:
                    return "1S"
                a[i] == "i"
                if a == b:
                    return "1S"
                a[i] == "j"
                if a == b:
                    return "1S"
                a[i] == "k"
                if a == b:
                    return "1S"
                a[i] == "l"
                if a == b:
                    return "1S"
                a[i] == "m"
                if a == b:
                    return "1S"
                a[i] == "n"
                if a == b:
                    return "1S"
                a[i] == "ñ"
                if a == b:
                    return "1S"
                a[i] == "o"
                if a == b:
                    return "1S"
                a[i] == "p"
                if a == b:
                    return "1S"
                a[i] == "q"
                if a == b:
                    return "1S"
                a[i] == "r"
                if a == b:
                    return "1S"
                a[i] == "s"
                if a == b:
                    return "1S"
                a[i] == "t"
                if a == b:
                    return "1S"
                a[i] == "u"
                if a == b:
                    return "1S"
                a[i] == "v"
                if a == b:
                    return "1S"
                a[i] == "w"
                if a == b:
                    return "1S"
                a[i] == "x"
                if a == b:
                    return "1S"
                a[i] == "y"
                if a == b:
                    return "1S"
                a[i] == "z"
                if a == b:
                    return "1S"
            return "+1"   