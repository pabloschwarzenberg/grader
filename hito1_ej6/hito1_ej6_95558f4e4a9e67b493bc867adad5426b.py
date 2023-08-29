X = int(input(''))
Y = int(input(''))
Z = int(input(''))
Max = max(X,Y,Z)
Min = min(X,Y,Z)
D = (X + Y +Z) - Max - Min
print(Min,',',D,',',Max)