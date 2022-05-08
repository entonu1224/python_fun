#A company has determined that its annual profit is typically 23 percent of total sales. Write
#a program that asks the user to enter the projected amount of total sales, and then displays
#the profit that will be made from that amount.
sales=float(input("enter  the projected amount of total sales.  "))
profit=(23/100)*sales
print ("profit is ", format(profit, ".2f"))