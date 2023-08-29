d=int(input("dia"))
m=int(input("mes"))
if((m==3 and 21<=d<=31) or (m==4 and 1<=d<=20)):
 print("aries")
elif((m==4 and 20<d<=30) or (m==5 and 1<=d<=21)):
 print("tauru")
elif((m==5 and 21<d<=31) or (m==6 and 1<=d<=21)):
 print("geminis")
elif((m==6 and 21<d<=30) or (m==7 and 1<=d<=23)):
 print("cancer")
elif((m==7 and 23<d<=31) or (m==8 and 1<=d<=23)):
 print("leo")
elif((m==8 and 23<d<=30) or (m==9 and 1<=d<=23)):
 print("virgo")
elif((m==9 and 23<d<=31) or (m==10 and 1<=d<=23)):
 print("libra")
elif((m==10 and 23<d<=30) or (m==11 and 1<=d<=22)):
 print("escorpio")
elif((m==11 and 23<d<=30) or (m==12 and 1<=d<=22)):
 print("sagitario")
elif((m==12 and 22<d<=31) or (m==1 and 1<=d<=20)):
 print("capricornio")
elif((m==1 and 20<d<=31) or (m==2 and 1<=d<=19)):
 print("acuario")
elif((m==2 and 19<d<=28) or (m==3 and 1<=d<21)):
 print("piscis")