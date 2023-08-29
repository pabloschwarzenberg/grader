#Ordenar tres números
n1=int(input("insertar numero"))
n2=int(input("insertar numero 2"))
n3=int(input("insertar numero 3"))
nma=max(n1,n2,n3)
nmi=min(n1,n2,n3)
me=(n1+n2+n3)-(nma+nmi)
print(nmi,",",me,",",nma)