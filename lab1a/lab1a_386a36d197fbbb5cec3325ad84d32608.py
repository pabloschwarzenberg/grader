cod1=input()
cod2=input()
cod3=input()
cod4=input()
cod5=input()
cod6=input()
total=int(cod1)+int(cod2)+int(cod3)
if  float(int(cod4)/int(cod1))>=0.8 or float(int(cod5)/int(cod2))>=0.8 or float(int(cod6)/int(cod3))>=0.8:
print ("senadora electa")
elif float((int(cod1)+int(cod2))/total)>=0.7 or float((int(cod3)+int(cod2))/total)>=0.7 or float((int(cod1)+int(cod3))/total)>=0.7:
print (" senadora electa")
elif float((int(cod1)+int(cod2)+int(cod3))/total)>=0.4:
print (" senadora electa")
else: 
print ("candidata perdedora")