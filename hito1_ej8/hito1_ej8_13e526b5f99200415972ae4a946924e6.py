num = int(input("Ingrese Un Número de 4 Cifras : "))
umil=(num-(num%1000))/1000
res = num%1000
cen = (res-(res%100))/100
res2 = res%100
dec = (res2-(res2%10))/10
uni = res2%10
if umil == 0 :
    print(cen,"C+",dec,"D+",uni,"U")
elif umil == 0 and cen == 0:
    print(dec,"D+",uni,"U")    
elif umil == 0 and cen == 0 and dec == 0:
    print(uni,"U")
else:        
    print(umil,"M+",cen,"C+",dec,"D+",uni,"U")