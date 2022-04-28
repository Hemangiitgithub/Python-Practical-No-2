# Q7.Harshad no. between 1 to 100.

def check_harshad(number):
  remainder = 0
  digit_sum = 0
  check = False
  n = number
  while(n > 0):
    remainder = n % 10
    digit_sum = digit_sum + remainder
    n = n//10
  if number % digit_sum == 0:
    check = True
  return check
lower = int(input("ENTER LOWEST NUMBER : "))
upper = int(input("ENTER HIGHEST NUMBER : "))
print("HARSHAD NUMBERS WITHIN RANGE({},{}) ARE -".format(lower,upper))
for i in range(lower,upper+1):
  if check_harshad(i):
    print(i,end = " ")

