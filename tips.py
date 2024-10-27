# define known values
food_cost=79.25
tax=6.54
tip=12.00

# calculate the unknown
total_due=food_cost+tax+tip
# The str()function is to cast a number into a string. It is being used here to cast the total due numerical value into a string value as we can not concatenate both a numerical value and a string value together. We would have to convert one data type into another.
# print("The total due is " + str(total_due))

# display the results
print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))

# bonus question
# you can't simply copy and past the above text into VSCode because it does not evaluate the strings with the variables.
# print(“Food cost is ” + str(food_cost) + “ and tax is ” + str(tax)) 
# print(“Tip is ” + str(tip)) 
# print(“Total due is ” + str(total_due)) 

