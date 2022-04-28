# Q2. Check the no. is Harshad or not.

t=input("Enter the No.: ")
sum = 0
for i in t:
    sum=sum+int(i)
if int(t)%sum==0:
    print(t,"its a Harshad no.")
else:
    print(t,"its not a Harshad no.")
    
