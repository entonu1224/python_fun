#Dr. Suarez teaches a literature class and uses the following 10-point grading scale for all of
#his exams
from re import A


score=float(input("enter your score..."))
a=90
b=80
c=70
d=60
if (score>=a):
    print ( "A")
else:
    if(score>=b):
        print ("B")
    else:
        if (score>=c):
            print("C")
        else:
            print("F")