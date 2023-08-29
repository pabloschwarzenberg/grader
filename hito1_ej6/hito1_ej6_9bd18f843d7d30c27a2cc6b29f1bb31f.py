a = int(input(''))
b = int(input(''))
c = int(input(''))
Max = max(a,b,c)
Min = min(a,b,c)
D = (a + b + c) - Max - Min
print(Min,',',D,',',Max)