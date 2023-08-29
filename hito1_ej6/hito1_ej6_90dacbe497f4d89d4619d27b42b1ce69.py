#Ordenar tres números
#Ordenar tres números
aa = int(input("Dijite el primer número: "))
bb = int(input("Dijite el segundo número: "))
cc = int(input("Dijite el tercer número: ")) 
if(aa<=bb and bb<=cc):
  print(aa,", ",bb,", ",cc)
elif(aa<=cc and cc<=bb):
  print(aa,", ",cc,", ",bb)
elif(bb<=aa and aa<=cc):
  print(bb,", ",aa,", ",cc)
elif(bb<=cc and cc<=aa):
  print(bb,", ",cc,", ",aa)
elif(cc<=aa and aa<=bb):
  print(cc,", ",aa,", ",bb)
elif(cc<=bb and bb<=aa):
  print(cc,", ",bb,", ",aa)