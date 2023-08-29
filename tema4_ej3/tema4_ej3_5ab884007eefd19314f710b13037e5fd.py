def jerigonzo(string):
    string=string.lower()
    string=list(string)
    q=len(string)
    i=0
    while  i<q:
      if "a"==string[i]:
        string.insert(i+1,"pa")
        i=i+1
        q=q+1
        continue
      elif "e"==string[i]:
        string.insert(i+1,"pe")
        i=i+1
        q=q+1
        continue
      elif "i"==string[i]:
        string.insert(i+1,"pi")
        i=i+1
        q=q+1
        continue
      elif "o"==string[i]:
        string.insert(i+1,"po")
        i=i+1
        q=q+1
        continue
      elif "u"==string[i]:
        string.insert(i+1,"pu")
        i=i+1
        q=q+1
        continue
      else:
        i=i+1
    string="".join(string)
    return string


if __name__ == "__main__":
    pass
         