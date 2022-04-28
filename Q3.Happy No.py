# Q3.Check Happy no. or not.

num1=input()
x=int(num1)
while (len(str(x))>1):
    sum=0
    num2=str(x)
    for i in range(len(num2)):
        sum=sum+(int(num2[i])**2)
    x=sum
if x==1:
    print("It is a Happy no.")
else:
    print("It is not Happy no.")
    
