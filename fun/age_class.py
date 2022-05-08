#Write a program that asks the user to enter a person’s age. The program should display
#a message indicating whether the person is an infant, a child, a teenager, or an adult.
#Following are the guidelines:
age=float (input(" enter your age.. "))
age_com1=0
age_comp2=1 
age_comp3=13
age_comp4=20
if (age>=0 and age<=1 ):
     print(" you are infiant")
elif(age >1 and age<13 ):
    print (" you are a child")
elif( age>=13 and age<20):
    print ("tennager")
else:
    print("adult")
