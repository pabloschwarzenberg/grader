def jerigonzo(string):
    string_jerigonzo =""
    vocales = ['a', 'e', 'i', 'o', 'u']    
    for i in string:
      if i in vocales:
        string_jerigonzo = string_jerigonzo+i+'p'+i
      else:
        string_jerigonzo = string_jerigonzo+i
    return string_jerigonzo

if __name__ == "__main__":
    pass
         