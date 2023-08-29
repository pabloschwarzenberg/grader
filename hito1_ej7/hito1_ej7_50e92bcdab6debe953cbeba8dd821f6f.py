#Zodiaco

y=eval(input('Ingrese día de número de día de sus nacimiento:'))
x=eval(input('Ingrese mes de su nacimiento:'))



if x== 1 and 31>=y>20  or x== 2 and 19>y>=1:
    print('Acuario.')
elif x==2 and  19<y<=31 or x==3 and 21>y>=1:
    print('Piscis.')
elif x==3 and  31>=y>=21 or x== 4 and 20>y>=1:
    print( ' Aries')
elif x==4 and  31>=y>20 or x== 5 and 21>y>=1:
    print ('Tauro')
elif x==5 and 31>=y>21 or x==6 and  21>y>=1:
     print ('Geminis')
elif x== 6 and 31>=y>21 or x==7 and  23>y>=1:
     print (' Cancer')
elif x== 7 and 31>=y> 23 or x== 8 and 23>y>=1:
     print ('Leo')
elif x== 8 and 31>=y>23 or x== 9 and 23>y>=1:
    print(' Virgo')
elif x==9 and 31>=y>23 or x== 10 and 23>y>=1:
    print(' Libra')
elif x==10 and 31>=y>23  or x==11 and 22>y>=1:
    print(' Escorpion' )
elif x==11 and  31>=y>22 or x==12 and 22>y>=1:
    print(' Sagitario' )
if x==12 and 31>=y>22 or x==1 and 20>y>=1:
    print ('Capricornio' )