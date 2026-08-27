# Write a function is_prime(n) that returns True/False.

def isprime(n):
    if(n%2==0 or n%3==0 or n%4==0 or n%5==0 or n%6==0 or n%7==0 or n%8==0 or n%9==0 or n%10==0):
        return False
    elif(n%1==0 and n%n==0):
        return True
    else:
        print("enter correct value .")

n=int(input("enter a num : "))
print(isprime(n))
