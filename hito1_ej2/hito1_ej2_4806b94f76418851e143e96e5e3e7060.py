n=int(input("INGRESE NUMERO 8 DIGITOS POR FAVOR: "))
hora=int(input("INGRESE HORA: "))
n=str(n)
if hora>=0 and hora<=7:
   print("CONTESTAR")
elif hora<=14 and n[5:8]=="909":
   print("CONTESTAR")
elif hora>=17 and hora <=19 and n[0:3]!="877":
   print("CONTESTAR")
else: 
   print("NO CONTESTAR") 
