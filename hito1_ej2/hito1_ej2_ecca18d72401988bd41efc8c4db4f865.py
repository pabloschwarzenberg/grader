#Contestador de celular
LL = int(input("num"))
HLL = int(input("hora"))

millones10 = LL// 10000000
mil = LL// 1000
CE = LL// 100 -mil*10 
DE =LL// 10 - mil*100 - CE*10
UN = LL// 1 - mil*1000 - CE*100 - DE*10 


print(millones10)
print(CE)
print(DE)
print(UN)

if HLL <= 7 : 
  print("contestar")
elif HLL <= 14 or CE == 9 and DE == 0 and UN == 9 :
  print("contestar")
elif 17 <= HLL <= 19 or millones10 == 8 :
  print("no contestar")
elif HLL <= 24 :
  print("no contestar")