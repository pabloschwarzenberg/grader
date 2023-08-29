#Descomponer un número
n = str(input())
if len(n) == 4 :
 a = n[3]
 b = n[2]
 c = n[1]
 d = n[0]
 m = d + "M"
 cc = c + "C"
 d = b + "D"
 u = a + "U"
 print (m, "+", cc, "+", d, "+", u)
elif len(n) == 3 :
 b = n[2]
 c = n[1]
 d = n[0]
 cc = d + "C"
 d = c + "D"
 u = b + "U"
 print (cc, "+", d, "+", u)
elif len(n) == 2 :
 c = n[1]
 d = n[0]
 d = d + "D"
 u = c + "U"
 print (d, "+", u)
elif len(n) == 1 :
 d = n[0]
 u = d + "U"
 print (u)