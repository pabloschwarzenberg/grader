#Contestador de celular
numero=int(input())
hora=int(input())
primeros3=numero//100000
ultimos3=numero-(numero//1000)*1000
if hora>=0 and hora<=7:
  print("CONTESTAR")
elif hora<14 and ultimos3:
  print("CONTESTAR")
elif hora<14 and ultimos3==false:
  print("NO CONTESTAR")
elif hora>=17 and hora<=19 and primeros3:
  print("NO CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")
  
