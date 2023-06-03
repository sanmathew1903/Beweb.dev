import random 
print("Welcome to the dice roller:")
while(1):
    print(random.randint(1,6))
    s=input("do u want to contiue: (Y/N)")
    if(s.lower()!="y"):
        break
        
