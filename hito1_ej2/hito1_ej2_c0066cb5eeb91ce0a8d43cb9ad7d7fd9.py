#Contestador de celular
numero=int(input())
hora=int(input())
primeros=numero//100000
ultimos=numero-(numero//1000)*1000
if hora>=0 and hora <=7:
  print("CONTESTAR")
elif hora <14 and ultimos:
  print("CONTESTAR")
elif hora <14 and ultimos==false:
     print("NO CONTESTAR")
elif hora>=17 and hora<=19 and primeros:
  print("NO CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")