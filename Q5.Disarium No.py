# Q5.Check the Disarium No. or not

num = int(input())
rem = s = 0;    
len = len(str(num))
     
#Makes a copy of the original number num    
n = num;    
     
#Calculates the sum of digits powered with their respective position    
while(num > 0):    
    rem = num%10;    
    s += int(rem**len);    
    num = num//10;    
    len -= 1;    
     
#Checks whether the sum is equal to the number itself    
if(s == n):    
    print( n,"is a disarium number");    
else:    
    print(n," not a disarium number");
