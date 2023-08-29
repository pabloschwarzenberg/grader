def jerigonzo(string):
    vocales=["a", "e", "i", "o", "u" ]
    for i in vocales:
        if string.find(i)!=-1:
          string = string.replace(i,i+"p"+i)
    return string
    
if __name__ == "__main__":
    pass
         