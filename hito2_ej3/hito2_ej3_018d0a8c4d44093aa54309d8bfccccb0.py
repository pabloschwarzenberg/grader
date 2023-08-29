mensaje=input()
n=3
if (len(mensaje)%n)!=0:
    print("ninguna")
if (len(mensaje)%n)==0:
    if len(mensaje)==3:
        print(mensaje[0]+mensaje[1]+mensaje[2])
    elif len(mensaje)==6:
        print(mensaje[1]+mensaje[2]+mensaje[0])
        print(mensaje[5]+mensaje[3]+mensaje[4])
    elif len(mensaje)==9:
        print(mensaje[0]+mensaje[1]+mensaje[2])
        print(mensaje[3]+mensaje[4]+mensaje[5])
        print(mensaje[6]+mensaje[7]+mensaje[8])            