assets=int(input("enter total amount of money you own or control?"))
print(assets)
debts=int(input("enter total amount of money you owe or due to another party"))
print(debts)

net_worth=assets-debts

print("Your net worth is " + "{:,}".format(net_worth))

# A pitfall would be that I needed to use casting of the correct data type to convert the string to an integer for my script to run
# As I experimented with different input values I could not enter floats and I could not enter text as a value it had to be an integer






