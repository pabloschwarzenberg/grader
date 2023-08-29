def jerigonzo(string):
    xd = [str(x) for x in str(string)] 
    contador = 0
    for x in xd:
        contador += 1
        if x in ["a", "e", "i", "o", "u"]:
            xd.insert(contador, "p"+x)
        else:
            continue
    return "".join(xd)

if __name__ == "__main__":
  plb = input()
  print(jerigonzio(plb))

         