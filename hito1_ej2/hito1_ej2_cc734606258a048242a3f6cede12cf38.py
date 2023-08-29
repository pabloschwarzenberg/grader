x=str(input())
y=int(input())
print(x[0:2])
if y < 8 and y >= 0:
     print('contestar')
elif y < 17 and y > 7:
     if x[5:8]=='909':
          print('contestar')
     else:
          print('no contestar')
elif y > 16 and y < 20:
     if x[0:3]=='877':
          print('no contestar')
     else:
          print('contestar')
else:
     print('no contestar')