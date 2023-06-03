import random
n=int(input("Enter an integer"))
while(1):
    s=random.randint(0,100)
    if(s==n):
        print("Your number was ",s)
        break
