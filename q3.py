#Take three numbers and print the largest of the three using if-else.
n1=int(input("enter n1 : ")) 
n2=int(input("enter n2 : "))
n3=int(input("enter n3 : "))
if(n1>n2 and n1>n3):
    print("the largest is : ", n1)
elif(n2>n1 and n2>n3):
    print("the lagest is : ", n2)
else:
    print("the largest is : ", n3)
