import math
amt_of_ppl=int(input(" How many people are going on the ghost tour? "))
amt_of_vans=float(amt_of_ppl/15)
cost_to_rent=float(amt_of_vans*250)
cost_per_person=float(cost_to_rent/15)
print("If there are", amt_of_ppl, "attendees you will need", math.ceil(amt_of_vans), "vans and it will cost", format(cost_to_rent, ".2f"), "to rent the vans but if you split it per person it will cost", format(cost_per_person, ".2f")) 

# My script said I had to charge 42.22 per person vs my calculations by hand said 19.74
# If I multiply that amount out, I would collect 1,604.36
# The vans were 633.33
# I have leftover money because my script calculated the decimal value of the amount of vans by 250.