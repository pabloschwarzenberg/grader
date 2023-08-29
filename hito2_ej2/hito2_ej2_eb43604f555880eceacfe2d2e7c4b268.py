string=input()
a=list(string)
x=a.count("A")+a.count("C")+a.count("T")+a.count("G")+a.count("a")+a.count("c")+a.count("t")+a.count("g")
if x==len(string):
  print( "secuencia correcta")
else:
  print( "secuencia incorrecta")