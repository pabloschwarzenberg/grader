def jerigonzo(string):
  while len(string)>0:
    if string.count("a")>=1:
      string=string.replace("a","apa")
    if string.count("e")>=1:
      string=string.replace("e","epe")
    if string.count("i")>=1:
      string=string.replace("i","ipi")
    if string.count("o")>=1:
      string=string.replace("o","opo")
    if string.count("u")>=1:
      atring=string.replace("u","upu")
    else:
      break
  return string