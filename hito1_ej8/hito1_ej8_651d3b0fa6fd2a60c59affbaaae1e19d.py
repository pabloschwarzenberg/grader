b=int(input())    
M=b//1000 
C=(b//100) - M*10
D=b//10 - C*10 - M*100
U= b - M*1000 - C*100 - D*10
print("{0}M+{1}C+{2}D+{3}U".format(M,C,D,U))