a=int(input("Enter first number between 1-10 "))
if(((a>10) or (a<1))):
    print('Seriously dude?')
b=int(input("Enter second number between 1-10 "))
if(((b>10) or (b<1))):
    print('Oh come on!!')
z= a+b
final=z+30
print('Final result after adding 30 to the sum is {}' .format(final))