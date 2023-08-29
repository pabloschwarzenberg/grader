def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    str_final=[]
    for i in string:
      if i not in vocales:
        str_final.append(i)
      if i in vocales:
        str_final.append(i)
        str_final.append("p")
        str_final.append(i)  
      string="".join(str_final)
    
    return string

if __name__ == "__main__":
    pass
         