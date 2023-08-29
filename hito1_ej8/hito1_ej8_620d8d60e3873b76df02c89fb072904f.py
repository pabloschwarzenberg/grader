num = int(input("Ingrese Un Número de hasta 4 Cifras : "))
m = round((num-(num%1000))/1000)
r = num%1000
c = round((r-(r%100))/100)
r = num%100
d = round((r-(r%10))/10)
u = round(r%10)

if m==0 and c == 0 and d == 0:
    print('{}U'.format(u))

elif m == 0 and c == 0:
    print('{}D + {}U'.format(d, u))

elif m == 0:
    print('{}C + {}D + {}U'.format(c, d, u))

else:
    print('{}M + {}C + {}D +{}U'.format(m, c, d, u))