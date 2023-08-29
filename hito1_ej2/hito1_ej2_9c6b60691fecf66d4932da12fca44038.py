#Contestador de celular
x=int(input("numero:"))
h=int(input("hora:"))
pri=int((x-x%10000000)/10000000)
seg=int(((x-pri*10000000)-(x-pri*10000000)%1000000)/1000000)
ter=int(((x-pri*10000000-seg*1000000)-(x-pri*10000000-seg*1000000)%100000)/100000)
uni=int(x%10)
dec=int(((x-x%10)%100)/10)
cen=int(((x-dec*10-uni)%1000)/100)
if h>0 and h<7:
 print("CONTESTAR")
elif h>7 and h<14 and (cen==9 and dec==0 and uni==9):
 print("CONTESTAR")
elif h>17 and h<19 and not(pri==8 and seg==7 and ter==7):
 print("CONTESTAR")
else:
 print("NO CONTESTAR")
      