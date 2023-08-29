#Ordenar tres números
s1 = int(input("Escriba el número >>> "))
s2 = int(input("Escriba el número >>> "))
s3 = int(input("Escriba el número >>> "))

if(s1<=s2 and s2<=s3):
    print("",s1,", ",s2,", ",s3,)
elif(s2<=s1 and s1<=s3):
    print("",s2,", ",s1,", ",s3,)
elif(s3<=s2 and s2<=s1):
    print("",s3,", ",s2,", ",s1,)
elif(s2<=s3 and s3<=s1):
    print("",s2,", ",s3,", ",s1,)
elif(s3<=s1 and s1<=s2):
    print("",s3,", ",s1,", ",s2,)
elif(s1<=s3 and s3<=s2):
    print("",s1,", ",s3,", ",s2,)