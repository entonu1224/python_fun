# A customer in a store is purchasing five items. Write a program that asks for the price of
#each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
#Assume the sales tax is 7 percent.
iterm1=float(input("enter the price of iterm1.."))
iterm2=float(input("enter the price of iterm2.."))
iterm3=float(input("enter the price of iterm3  "))
iterm4=float(input("enter the price of iterms4.."))
iterm5=float(input("enter the price of iterm5"  ))
sub_total=iterm1+iterm2+iterm3+iterm4+iterm5
tax=(7/100)*sub_total
total=sub_total+tax
print("sales of iterms..", format(sub_total,  ".2f"))
print( "tax on the iterms ", tax)
print("total cost of iterms", total)

