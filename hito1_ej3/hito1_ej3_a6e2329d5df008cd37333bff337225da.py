#Aprobación de créditos
I = int(input())
AN = int(input())
NH = int(input())
AP = int(input())
EC = input()
CC = input()

Edad = 2014-AN

a = AP>10 and NH>=2
b = EC=="C" and NH>3 and (Edad>=45 and Edad<=55)
c = I>2500000 and EC =="S" and CC=="U"
d = I>3500000 and AP>5
e = CC=="R" and EC=="C" and NH<2
if a or b or c or d or e:
        print("APROBADO")
else:
        print("RECHAZADO")