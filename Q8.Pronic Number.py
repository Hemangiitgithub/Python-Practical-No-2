# Q8.Check number is pronic or not.

n = int(input("Enter a number: "))
f = 0
for i in range(n):
    if i * (i + 1) == n:
        f = 1
        break
if f==1:
    print(n,"is Pronic number")
else:
    print(n,"is Not a Pronic number")
