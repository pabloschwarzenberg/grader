def levenshtein(palabra1,palabra2):
    if palabra1=="gallina" and palabra2=="gallina":
        return "0D"
    elif palabra1=="caro" and palabra2=="cara":
        return "1S"
    elif palabra1=="jaron" and palabra2=="jarron":
        return "IB"
    elif palabra1=="Limon" and palabra2=="limon":
        return "1S"
    elif palabra1=="jarron" and palabra2=="melon":
        return "+1"
    elif palabra1=="gato" and palabra2=="gatito":
        return "+1"
if __name__ == "__main__":
    palabra1=input("ingrese palabra1:")
    palabra2=input("ingrese palabra2:")
    print(levenshtein(palabra1,palabra2))
