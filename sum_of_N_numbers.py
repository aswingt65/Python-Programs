n = int(input("Enter value of n: "))
if n >= 0:
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    print("sum is: ",sum)
else:
    print("Please enter a positive number")