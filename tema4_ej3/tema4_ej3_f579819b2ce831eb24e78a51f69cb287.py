def jerigonzo(string):
    l=list(string)
    f = []
    for i in range(0,len(l)):
      if l[i] in ["a","e","i","o","u"]:
        f.append(str(l[i]))
        f.append("p")
        f.append(str(l[i]))
      else:
        f.append(str(l[i]))
    string = "".join(f)
    return string
    
if __name__ == "__main__":
    pass
         