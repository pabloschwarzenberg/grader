def jerigonzo(string):
    a=list(string)
    largo=len(a)
    vocales="aeiou"
    for i in range(0,largo):
      if a[i] in vocales:
        a.insert(i+1,"p")
        a.insert(i+2,a[i])
    return "".join(a)

if __name__ == "__main__":
    pass
         