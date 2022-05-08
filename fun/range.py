#Write an if statement that checks if the value a lies in the range of 10 to 30 and
#assigns the value of the variable a to 20.
a=int(input("enter a value"))
num1=10; num2=30
if (a>=10 and a<=30):
    a=20
    print (" the new value is  ", a)
else:
    print("number out of range")