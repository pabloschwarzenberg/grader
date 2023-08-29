six=input("Numbers:  ")
terminos=[x for x in six.split()]
print(terminos)

a=int(terminos[0])
b=int(terminos[1])
c=int(terminos[2])
d=int(terminos[3])
e=int(terminos[4])
f=int(terminos[5])

y=(c-(a*f)/d)/(b-(a*e)/d)
x=(f-(e*y)/d)