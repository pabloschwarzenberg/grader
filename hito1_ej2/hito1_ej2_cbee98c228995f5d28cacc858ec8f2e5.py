#Contestador de celular
x=int(input('Ingrese un número telefonico "8 cifras"'))
if 10000000<=x and x<=99999999:
        h=int(input('ingrese la hora entre "0 y 23"'))
        if h>=0 and h<=23:
                if h>=0 and h<=7:
                        print('CONTESTAR')
                if h<14 and h>8:
                         if (x%10)==9 and ((x//10)%10)==0 and ((x//100)%10)==9:
                                print('CONTESTAR')
                         else:
                                print('NO CONTESTAR')
                if h>=17 and h<=19:
                        if (x//10000000)==8 and ((x//1000000)%10)==7 and ((x//100000)%10)==7:
                                 print('NO CONTESTAR')
                        else:
                                 print('CONTESTAR')
                if h>19 and h<23:
                        print('NO CONTESTAR')
        else:
                print('ingrese un número entre 0 y 23')
else:
        print('ingrese un número de 8 cifras')
