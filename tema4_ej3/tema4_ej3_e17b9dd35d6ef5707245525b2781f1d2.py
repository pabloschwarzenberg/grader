def jerigonzo(string):
    a = []
    for e in string:
      for l in e:
        if l in "aeiou":
          l = l + "p" +l
        a.append(l)
    a = "".join(a)
    return a

if __name__ == "__main__":
    pass
         