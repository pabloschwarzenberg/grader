#Zodiaco
a= ["capricornio", "acuario", "piscis", "aries", "tauro", "geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario"]
b= (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
m=[1,2,3,4,5,6,7,8,9,10,11,12]
d=int(input("dia:"))
m=int(input("mes:"))
m=m-1
if d>b[m]:
   m=m+1
if m==12:
   m==0
print(a)