# Write a function factorial(n) that computes factorial using a loop
a = int(input("Enter num: "))
b = 1
while (a >= 1):
    b*=a
    a-=1
print(b)