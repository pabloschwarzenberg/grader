#Aprobación de créditos
i=int(input())
a=int(input())
n=int(input())
ap=int(input())
e=input()
v=input()


R=1
U=2
v=R or U
C=3
S=4
e=C or S


edad=2017-a

if ap>10 and n>=2 or e==C and n>=3 and 45<=edad<=55 or i>2500000 and e==S and v==U or i>3500000 and ap>5 or v==R and e==C and n<2:
    print("APROBADO")
else:
    print("RECHAZADO")