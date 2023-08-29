#Nota final
pt=float(input("PT: "))
pi=float(input("PI: "))
ne=float(input("NE: "))
pp=float(input("PP: "))
pf=0.3*pt+0.3*pi+0.3*ne+0.1*pp
rpf1=pf%0.1
rpf2=pf%0.01
rrpf=rpf1-rpf2
if rrpf>=0.05:
  pfaprox=pf-rpf1+0.1
else :
  pfaprox=pf-rpf1
print("PF:",pfaprox)