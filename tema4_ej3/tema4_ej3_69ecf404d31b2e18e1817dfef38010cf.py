def jerigonzo(string):
    string_final=""
    for x in string:
      if x == "a":
          string_final = string_final + "apa"
      elif x == "e":
          string_final = string_final + "epe"
      elif x == "i":
          string_final = string_final + "ipi"
      elif x == "o":
          string_final = string_final + "opo"
      elif x == "u":
          string_final = string_final + "upu"
      else:
          string_final = string_final + x
    return string_final
   

if __name__ == "__main__":
    pass
         