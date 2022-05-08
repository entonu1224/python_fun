#Kathryn teaches a science class and her students are required to take three tests. She wants
#to write a program that her students can use to calculate their average test score. She also
#wants the program to congratulate the student enthusiastically if the average is greater
#than 95. Here is the algorithm in pseudocode:
test1=float(input("enter the first test score  "))
test2=float(input("enter the second test score "))
test3=float(input("enter the third test score  "))
total_score=test1+test2+test3
avg=total_score/3
max_avg=95
if avg>max_avg:
    print("congratulation  you have done well " )
print(" your average is", avg)