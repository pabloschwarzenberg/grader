#Descomponer un número
numero=int(input("Ingrese un numero entero:\n"))
umil=(numero%10000-numero%1000)//1000
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10

# umil = numero / 1000
# tmp = numero % 1000
# centenas = tmp / 103
# tmp = tmp % 100
# decenas = tmp / 10
# unidades = tmp % 10

# umil=round(umil)
# centenas=round(centenas)
# decenas=round(decenas)
# unidades=round(unidades)
umil="{0:.0f}".format(umil)
centenas="{0:.0f}".format(centenas)
decenas="{0:.0f}".format(decenas)
unidades="{0:.0f}".format(unidades)
longitudNumero=len(str(numero))
if longitudNumero==4:
    print(umil,"M+",centenas,"C+",decenas,"D+",unidades,"U", sep='')
elif longitudNumero==3:
    print(centenas,"C+",decenas,"D+",unidades,"U", sep='')
elif longitudNumero==2:
    print(decenas,"D+",unidades,"U", sep='')
elif longitudNumero==1:
    print(unidades,"U", sep='')