t1=float(input("Votos Comuna 1: "))
t2=float(input("Votos Comuna 2: "))
t3=float(input("Votos Comuna 3: "))

v1=float(input("Candidato Comuna 1: "))
v2=float(input("Candidato Comuna 2: "))
v3=float(input("Candidato Comuna 3: "))

p1=v1/t1
p2=v2/t2
p3=v3/t3
t=t1+t2+t3
v=v1+v2+v3

if p1>=0.8 or p2>=0.8 or p3>=0.8:
    print("electa")
elif (v1+v2)/t >=0.7 or (v2+v3)/t >= 0.7 or (v1+v3)/t >=0.7:
    print("electa")
elif v/t >= 0.4:
    print("electa")
else:
    print("perdedora")