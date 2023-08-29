#Descomponer un número
n=int(input("ingrese numero: "))
from math import floor

if n>999:
   m1=floor(n/1000)
   c1=floor((n%1000)/100)
   d1=floor(((n%1000)%100)/10)
   u1=floor(((n%1000)%100)%10)
   m11=str(m1)
   c11=str(c1)
   d11=str(d1)
   u11=str(u1)
   print(m11+('M+')+c11+('C+')+d11+('D+')+u11+('U'))

if 999>=n>=100:
   c2=floor(n/100)
   d2=floor((n%100)/10)
   u2=floor((n%100)%10)
   c22=str(c2)
   d22=str(d2)
   u22=str(u2)
   print(c22+('C+')+d22+('D+')+u22+('U'))

if 99>=n>9:
   d3=floor(n/10)
   u3=floor(n%10)
   d33=str(d3)
   u33=str(u3)
   print(d33+('D+')+u33('U'))
  
if n<10:
   u4=n
   u44=str(u4)
   print(u44+('U'))


