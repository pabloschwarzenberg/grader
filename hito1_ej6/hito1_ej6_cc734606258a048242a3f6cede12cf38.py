x=(input(''))
y=(input(''))
z=(input(''))
if x < y and y < z:
    print(x+','+y+','+z)
elif x < z and y < x:
    print(y+','+x+','+z)
elif z < y and y < x:
    print(z+','+y+','+x)
elif x < z and z < y:
    print(x+','+z+','+y)
elif y < z and z < x:
    print(y+','+z+','+x)
elif z < x and x < y:
    print(z+','+x+','+y)
elif x == y and x < z:
    print(x+','+y+','+z)
elif x == z and x < y:
    print(x+','+z+','+y)
else:
    print(y+','+x+','+z)