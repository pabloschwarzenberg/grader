#Contestador de celular
n=int(input("numero:"))
hora=int(input("hora:"))
primero=int((n-n%10000000)/10000000)
segundo=int(((n-primero*10000000)-(n-primero*10000000)%1000000)/1000000)
tercero=int(((n-primero*10000000-segundo*1000000)-(n-primero*10000000-segundo*1000000)%100000)/100000)
u=int(n%10)
d=int(((n-n%10)%100)/10)
c=int(((n-d*10-u)%1000)/100)
if hora>0 and hora<7:
 print("CONTESTAR")
elif hora>7 and hora<14 and (c==9 and d==0 and u==9):
 print("CONTESTAR")
elif hora>17 and hora<19 and not(primero==8 and segundo==7 and tercero==7):
 print("CONTESTAR")
else:
 print("NO CONTESTAR")