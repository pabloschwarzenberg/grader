def jerigonzo(string):
    Vocales = ["a","e","i","o","u","A","E","I","O","U"]
    Final = ""
    for L in string:
      if L in Vocales:
        Final = Final + L + "p" + L
      else:
        Final = Final + L
    return Final         