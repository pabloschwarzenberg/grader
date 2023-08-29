x1 = eval(input())
y1 = eval(input())
n1 = eval(input())
x2 = eval(input())
y2 = eval(input())
n2 = eval(input())
mltp = x1/x2
y2 = (y2*-mltp)+(y1)
n2 = (n2*-mltp)+(n1)
y = n2/y2
x = (n1-(y1*y))/x1
x = round(x, 1)
y = round(y, 1)
answer = ["x="+ str(x) , "y="+str(y)]
print(answer)