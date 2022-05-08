ans=input("enter a 'y' to satart the program ")
respond="y"
total=0
while (respond==ans):
    num=float(input ('enter a value'))
    total=total+num
    ans=input("enter 'y' to continue  and any other value to display the result  ")

print(total)
