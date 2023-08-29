def jerigonzo(string):
 f = ""
 for p in string:
  f += p
  if p.lower() in "aeiou":
    f += "p" + p
 return f