def jerigonzo(palabra):
  l = list(palabra)
  c = 0 
  r = ""
  for a in palabra:
      if l(c) == "a":  
        r += "apa"
      elif l(c)=="e":
        r += "epe"
      elif l(c)=="i":
        r += "ipi"
      elif l(c)=="o":
        r += "opo"
      elif l(c)=="u":
        r += "upu"
   else:
        r += l(c)
      c += 1
return r
    