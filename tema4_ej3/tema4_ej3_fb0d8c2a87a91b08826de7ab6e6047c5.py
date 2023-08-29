def jerigonzo(string):
  g=0
  s=list(string)
  while g<len(s):
    if s[g]=="a":
      s.insert(g+1,"p")
      s.insert(g+2,"a")
      g=g+3
    elif s[g]=="e":
      s.insert(g+1,"p")
      s.insert(g+2,"e")
      g=g+3
    elif s[g]=="i":
      s.insert(g+1, "p")
      s.insert(g+2,"i")
      g=g+3
    elif s[g]=="o":
      s.insert(g+1,"p")
      s.insert(g+2,"o")
      g=g+3
    elif s[g]=="u":
      s.insert(g+1, "p")
      s.insert(g+2,"u")
      g=g+3
    g=g+1

  final="".join(s)
  return final
