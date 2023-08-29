def jerigonzo(string):
  l=list(string)
  l1=len(l)
  a1=l.count("a")
  e1=l.count("e")
  i1=l.count("i")
  o1=l.count("o")
  u1=l.count("u")
  suma=a1+e1+i1+o1+u1
  i=0
  while i<(l1+(2*suma)-1):
    if (l[i]=="a") or (l[i]=="e") or (l[i]=="i") or (l[i]=="o") or (l[i]=="u"):
      if l[i]=="a":
        l.insert(i+1,"p")
        l.insert(i+2,"a")
        i+=2
      if l[i]=="e":
        l.insert(i+1,"p")
        l.insert(i+2,"e")
        i+=2
      if l[i]=="i":
        l.insert(i+1,"p")
        l.insert(i+2,"i")
        i+=2
      if l[i]=="o":
        l.insert(i+1,"p")
        l.insert(i+2,"o")
        i+=2
      if l[i]=="u":
        l.insert(i+1,"p")
        l.insert(i+2,"u")
        i+=2
    i+=1
  string=""
  for i in range(len(l)):
    string+=l[i]
  return string
         