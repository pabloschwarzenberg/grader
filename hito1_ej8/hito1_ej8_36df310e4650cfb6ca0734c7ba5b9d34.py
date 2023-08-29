num = int(input("Ingrese Un Número de 4 Cifras : "))
mil = (num-(num%1000))/1000
cen = (num-(num%100))/100
res = num%100
dec = (res-(res%10))/10
uni = res%10
if num>=1000:
    print(f"{str(mil)}M + {str(cen)}C + {str(dec)}D + {str(uni)}U")
elif num>=100:
    print(f"{int(cen)}C + {int(dec)}D + {int(uni)}U")
elif num>=10:
    print(f"{int(dec)}D + {int(uni)}U")
elif num>=1:
    print(f"{int(uni)}U")
else:
    print("false")
