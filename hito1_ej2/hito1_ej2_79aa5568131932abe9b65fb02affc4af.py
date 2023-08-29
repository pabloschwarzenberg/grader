numero=int(input())
hora=int(input())
nfinal=(numero%1000)
nprincipio=(numero//100000)
if hora>=0 and hora<=7:
   print("CONTESTAR")
elif hora>7 and hora<14:
  if nfinal==909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif hora>=14 and hora<15:
  print("NO CONTESTAR")
elif hora>=17 and hora<=19:
  if nprincipio==877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif hora>19 and hora<=23:
  print("NO CONTESTAR")
