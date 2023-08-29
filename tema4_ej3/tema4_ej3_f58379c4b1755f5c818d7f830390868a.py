def jerigonzo(string):
    translate = ""
    for letra in string:
      if letra in "aeiouAEIOU":
        translate = translate + letra
        translate = translate + "p"
      translate = translate + letra
    return translate
