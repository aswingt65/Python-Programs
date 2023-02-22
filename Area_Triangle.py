a = float(input("Enter the 1st Side : "))
b = float(input("Enter the 2nd side : "))
c = float(input("Enter the 3rd Side : "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the given triangle is",area)