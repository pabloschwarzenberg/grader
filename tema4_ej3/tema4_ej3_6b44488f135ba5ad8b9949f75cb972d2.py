def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    a=list(string)
    for vocal in vocales:
      for i in range(len(a)):
        if vocal==a[i]:
          a[i]=vocal+"p"+vocal
    string="".join(a)
    return string

if __name__ == "__main__":
    texto=input()
    jerigonzo(texto)