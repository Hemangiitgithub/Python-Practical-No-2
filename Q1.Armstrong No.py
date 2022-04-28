# Armstrong Number:

t=int(input("Enter the no."))
sum = 0
temp=t
while temp>0:
    digit = temp%10
    sum+=digit**3
    temp//=10
if t==sum:
    print(t,"is an Armstrong no.")
else:
    print(t,"is not an Armstrong no.")
    
