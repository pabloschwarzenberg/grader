l1=[]
def des(num):
    for i in num:
        l1.append(int(i))
    return (l1)
num=(input("ingrese numero"))
l1=des(num)   
print(f"M:{l1[0]} + C:{l1[1]} + D:{l1[2]} + U:{l1[3]} ") 