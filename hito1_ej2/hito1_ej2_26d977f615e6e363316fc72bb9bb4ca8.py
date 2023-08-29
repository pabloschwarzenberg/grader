numero=int(input())
hora=int(input())

if hora>0 and hora<7:
  print("CONTESTAR")
elif hora<14 and numero%10**3==909:
  print("CONTESTAR")
elif hora<14 and numero%10**3!=909:
  print("NO CONTESTAR")
elif hora>=17 and hora<=19 and numero//10**5==877:
  print("NO CONTESTAR")
elif hora>=17 and hora<=19 and numero//10**5!=877:
  print("CONTESTAR")
elif hora>19:
  print("NO CONTESTAR")

      
      
  
  
  