#DIGITO RUT GGGGG



THERUTGG=int(input("Ingrese el rut: "))



manzanaH=(THERUTGG//10000000) * 3



manzanaG=((THERUTGG//1000000)%10) * 2



manzanaF=((THERUTGG//100000)%10) * 7



manzanaE=((THERUTGG//10000)%10) * 6



manzanaD=((THERUTGG//1000)%10) * 5



manzanaC=((THERUTGG//100)%10) * 4



manzanaB=((THERUTGG//10)%10) * 3



manzanaA=((THERUTGG//1)%10) * 2



MEGASUMAA=(manzanaH+manzanaG+manzanaF+manzanaE+manzanaD+manzanaC+manzanaB+manzanaA)



thefirstresto= MEGASUMAA // 11




resto2=MEGASUMAA-(11*thefirstresto)



MEGARESTAA=11-resto2



if MEGARESTAA == 11:

  print("dv=",end="")

  print(0)



elif MEGARESTAA == 10:

  print("dv=",end="")

  print("k")



else:

  print("dv=",end="")

  print(MEGARESTAA)