N1=int(input("numero uno: "))
N2=int(input("numero dos: "))
N3=int(input("numero tres: "))
NI= min (N1,N2,N3)
NF= max (N1,N2,N3)
NM=N1+N2+N3-NI-NF  
print (NI,",",NM,",",NF)