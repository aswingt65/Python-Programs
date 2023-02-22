num = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if num <= 0:
   print("Please enter a positive integer")
elif num == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < num:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count += 1