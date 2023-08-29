a = int(input("Ingrese el número a descomponer: "))

m = (a//1000)
u = (a%10)
c = (a - m*1000 - u)//100
d = (a - m*1000 - c*100 - u)//10


print("Número descompuesto: {}M + {}C + {}D + {}U".format(m, c, d, u))