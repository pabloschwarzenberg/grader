def jerigonzo(string):
  z=0
  s=list(string)
  while z<len(s):
    if s[z]=="a":
      s.insert(z+1,"p")
      s.insert(z+2,"a")
      z=z+3
    elif s[z]=="e":
      s.insert(z+1,"p")
      s.insert(z+2,"e")
      z=z+3
    elif s[z]=="i":
      s.insert(z+1, "p")
      s.insert(z+2,"i")
      z=z+3
    elif s[z]=="o":
      s.insert(z+1,"p")
      s.insert(z+2,"o")
      z=z+3
    elif s[z]=="u":
      s.insert(z+1, "p")
      s.insert(z+2,"u")
      z=z+3
    z=z+1

  final="".join(s)
  return final
         