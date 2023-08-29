#Contestador de celular
n=int(input())
h=int(input())
if 0<n<7:
 print("CONTESTAR")
elif 0<h<14 and ((n-909)%1000)==0:
 print("CONTESTAR")
elif 5<h<9 and 0>(n-87700000)>=100000:
 print("CONTESTAR")
else: print("NO CONTESTAR")
