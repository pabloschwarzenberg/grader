#Cálculo del dígito verificador de un rut
rut=int(input("RUT (PRIMEROS 8 DIGITOS): "))

ク=((rut//1)%10) * 2
キ=((rut//10)%10) * 3
カ=((rut//100)%10) * 4
オ=((rut//1000)%10) * 5
エ=((rut//10000)%10) * 6
ウ=((rut//100000)%10) * 7
イ=((rut//1000000)%10) * 2
ア=(rut//10000000) * 3


suma=(ア+イ+ウ+エ+オ+カ+キ+ク)
resto1= suma // 11
resto2=suma-(11*resto1)
resta=11-resto2


if resta == 11:
    print("dv=",end="")
    print(0)
elif resta == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(resta)
