#Chris owns an auto repair business and has several employees. If any employee works over
#40 hours in a week, he pays them 1.5 times their regular hourly pay rate for all hours over
#40. He has asked you to design a simple payroll program that calculates an employee’s
#gross pay, including any overtime wages. You design the following algorithm:__
hour =_w=int(input("enter the hour worked.."))
pay_r=float(input("enter the pay rate  "))
base_h=40
over_time_r=1.5
if (hour>=base_h):
    over_time_h=hour-base_h
    over_time_p=over_time_h*pay_r*over_time_r
    gross_p=(hour*pay_r)+over_time_p
    print ( "gross pay", gross_p)
else:
    normal_gross_pay=hour*pay_r
    print( "gross pay", normal_gross_pay)
