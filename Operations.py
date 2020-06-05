choice=int(input("Enter 1 for addition; 2 for subtraction; 3 for division; 4 for multiplication; 5 for Average: "))
if(choice==1):
    first=int(input("Enter first variable "))
    second=int(input("Enter second variable "))
    add=first+second
    print(add)
    if(add<0):
        print("zsa")
elif(choice==2):
    first=int(input("Enter first variable "))
    second=int(input("Enter second variable "))
    sub=first-second
    print(sub)
    if(sub<0):
        print("zsa")
elif(choice==3):
    first=int(input("Enter first variable "))
    second=int(input("Enter second variable "))
    div=first/second
    print(div)
    if(div<0):
        print("zsa")
elif(choice==4):
    first=int(input("Enter first variable "))
    second=int(input("Enter second variable "))
    mul=first*second
    print(mul)
    if(mul<0):
        print("zsa")
elif(choice==5):
    first1=int(input("Enter your first number "))
    second2=int(input("Enter your second number "))
    avg=(first1+second2)/2
    print(avg)
    if(avg<0):
        print("zsa")
else:
    print("You really need good glasses dude!!")