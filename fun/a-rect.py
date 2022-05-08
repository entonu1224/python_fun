#The area of a rectangle is the rectangle’s length times its width. Write a program that asks
#for the length and width of two rectangles. The program should tell the user which rectan-
#gle has the greater area, or if the areas are the same.

li=float(input("enter the lenght of the first rectsngle"))
w1=float(input("enter the width of the first rectsngle"))
l2=float(input ("enter the lenght of the second rectangle"))
w2=float(input("enter the width of the second rectangle"))
area_rec1=li*w1
area_rec2=l2*w2
if (area_rec1==area_rec2):
    print(" the two rectangle have the same area")
elif( area_rec1>area_rec2):
    print(" the area of  rectangle1 is greater than reactangle2")
else:
    print(" the area of  reactanle2 is grater than rectangle1  ")