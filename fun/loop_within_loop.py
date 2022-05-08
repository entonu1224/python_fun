#loop within loop
#the program takes one student the numbers of subjects and its score then display the average
num_of_s=int(input("enter the number of student "))
subject_no=int (input("enter the number of subject "))
def main():
    for student in range(  num_of_s):
        print("student id:", student)
        total=0
        for  course in range( subject_no ):
            score=float(input(" enter the subject score "))
            if (score >=0 and score<=100):
                total=total+score
                avg=total/subject_no
            else:
                print("enter a valid score ")
                score=float(input(" enter your score afain"))
                avg=total/subject_no
        print( "student iD", student,  avg)
        s_avg(  student, avg)

def s_avg(  student, avg):
    a=90
    b=80
    c=70
    d=60
    f=50
    up_limit=100
    if( avg>=a and avg<=up_limit):
        print ( student, 'grade: A')
    elif(avg>=b and avg<a):
        print (student, "grade : B")
    elif( avg>=c and avg<b):
        print ( student, "grade :C")
    elif(avg>=d and avg<c):
        print (" grade D" )
    else:
        print( "grade F")
main()
    


