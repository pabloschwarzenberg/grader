def jerigonzo(x):
    l=list(x)
    largo=len(l)+(l.count("a")+l.count("e")+l.count("i")+l.count("o")+l.count("u"))
    for i in range(0, largo):
      if l[i] in ["a","e","i","o","u"]:
        u=l.index(l[i])
        l.insert(i+1,"p"+str(l[i]))
      else:
        pass
    return str("".join(l))

         