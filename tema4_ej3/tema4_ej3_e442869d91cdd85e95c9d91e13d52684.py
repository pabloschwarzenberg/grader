def jerigonzo(string):
    palabra= ""
    vocales=["a","e","i","o","u"]
    for i in string:
      if i in vocales:
        palabra += i
        palabra += "p"
        palabra += i
      else:
        palabra += i
    
    
    return palabra

if __name__ == "__main__":
    pass
         