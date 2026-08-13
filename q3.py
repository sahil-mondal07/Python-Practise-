#Take three numbers and print the largest of the three using if-else.
n1 = int(input("enter n1 : "))
n2 = int(input("enter n2 : "))
n3 = int(input("enter n3 : "))

# Step 1: find the actual max value — nothing about ties yet
biggest = n1
if n2 > biggest:
    biggest = n2
if n3 > biggest:
    biggest = n3

# Step 2: NOW check how many numbers equal that max — this is where ties live
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