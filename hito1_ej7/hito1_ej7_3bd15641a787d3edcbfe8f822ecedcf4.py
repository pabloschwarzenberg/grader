#Zodiaco
from datetime import datetime
from collections import namedtuple
d=str(input("ingrese dia: "))
m=str(input("ingrese el mes: "))
Range=namedtuple("Range", ["start","end"])
a=1999
b=2000
dm= "m"+"d"


if m and d == Range(start=datetime(a, 3, 21), end=datetime(a, 4, 20)):
    print("aries")
else:
    if dm== Range(start=datetime(a, 4, 21), end=datetime(a, 5, 21)):
        print("tauro")
    else:
        if dm== Range(start=datetime(a, 5, 22), end=datetime(a, 6, 21)):
            print("geminis")
        else:
            if dm== Range(start=datetime(a, 6, 22), end=datetime(a, 7, 23)):
                print("cancer")
            else:
                if dm== Range(start=datetime(a, 7, 24), end=datetime(a, 8, 23)):
                    print("leo")
                else:
                    if dm== Range(start=datetime(a, 8, 24), end=datetime(a, 9, 23)):
                        print("virgo")
                    else:
                        if dm== Range(start=datetime(a, 9, 24), end=datetime(a, 10, 23)):
                            print("libra")
                        else:
                            if dm== Range(start=datetime(a, 10, 24), end=datetime(a, 11, 22)):
                                print("escorpion")
                            else:
                                if dm== Range(start=datetime(a, 11, 23), end=datetime(a, 12, 22)):
                                    print("sagitario")
                                else:
                                    if dm== Range(start=datetime(a, 12, 23), end=datetime(b, 1, 20)):
                                        print("capricornio")
                                    else:
                                        if dm== Range(start=datetime(b, 1, 21), end=datetime(b, 2, 19)):
                                            print("acuario")
                                        else:
                                            if dm== Range(start=datetime(b, 2, 20), end=datetime(b, 3, 20)):
                                                print("piscis")     