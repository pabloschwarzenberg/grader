dd=int(input("dia que nació:"))
mm=int(input("mes que nació:"))
import random

x=mm*30+dd
if x in range(79,110) :
   print("su signo zodiacal es piscis")
if x in range(51,78) :
   print("su signo zodiacal es acuario ")
if x in range(382,50) :
    print("su signo zodiacal es capricornio")
if x in range(353,381) :
    print("su signo zodiacal es sagitario")
if x in range(323,352) :
    print("su signo zodiacal es escorpio")
if x in range(293,322) :
    print("su signo zodiacal es libra")
if x in range(263,292) :
    print("su signo zodiacal es virgo")
if x in range(233,262) :
    print("su signo zodiacal es leo")
if x in range(202,232) :
    print("su signo zodiacal es cancer")
if x in range(171,201) :
    print("su signo zodiacal es geminis")
if x in range(141,170) :
    print("su signo zodiacal es tauro")
if x in range(111,140) :
    print("su signo zodiacal es aries")