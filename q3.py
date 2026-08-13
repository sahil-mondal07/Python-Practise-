#Take three numbers and print the largest of the three using if-else.
n1 = int(input("enter n1 : "))
n2 = int(input("enter n2 : "))
n3 = int(input("enter n3 : "))

biggest = n1
if n2 > biggest:
    biggest = n2
if n3 > biggest:
    biggest = n3
count = 0
if n1 == biggest:
    count += 1
if n2 == biggest:
    count += 1
if n3 == biggest:
    count += 1

if count > 1:
    print("largest value is", biggest, "but it's tied")
else:
    print("the largest is:", biggest)