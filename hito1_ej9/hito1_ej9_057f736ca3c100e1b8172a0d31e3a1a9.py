#Sistema de Ecuaciones
L1=[int(input(":")),int(input(":")),int(input(":"))]    
L2=[int(input(":")),int(input(":")),int(input(":"))] 
det=(L1[0]*L2[1])-(L2[0]*L1[1])
x=(((L1[2]*L2[1])-(L2[2]*L1[1]))/det).__round__(1)
y=-(((L1[2]*L2[0])-(L2[2]*L1[0]))/det).__round__(1)
print("x={0}".format(x))
print("y={0}".format(y))