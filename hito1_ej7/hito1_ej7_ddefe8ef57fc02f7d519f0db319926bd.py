#Zodiaco
dc = int(input())
mc = int(input())
m = { 1:0, 2:31, 3:59, 4:90, 5:120, 6:151, 7:181, 8:202, 9:233, 10:263, 11:294, 12:324 }
da = dc + int(m[mc])
if 80 <= da <= 110:
    print ("aries")
elif 111 <= da <= 141:
    print ("tauro")
elif 142 <= da <= 172:
    print ("geminis")
elif 173 <= da <= 203:
    print ("cancer")
elif 204 <= da <= 224:
    print ("leo")
elif 225 <= da <= 256:
    print ("virgo")
elif 257 <= da <= 286:
    print ("libra")
elif 287 <= da <= 316:
    print ("escorpion")
elif 317 <= da <= 345 :
    print ("sagitario")
elif 346 <= da or da <= 20:
    print ("capricornio")
elif 21 <= da <= 50:
    print ("acuario")
elif 51 <= da <= 79:
    print ("piscis")