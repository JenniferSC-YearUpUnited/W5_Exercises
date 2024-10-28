# calculate gross pay given the variables pay_rate and hours_worked. If the person works more than 40 hours, pay the overtime hours at 1.5 times the rate of regular hours. 

pay_rate=17.30
hours_worked=45
othours = 5
regross_pay= pay_rate * hours_worked
otgross_rate = (1.5 *pay_rate)* othours
otgross_pay = otgross_rate + regross_pay 
if hours_worked == 40:
    print("Your gross pay is $", regross_pay, "No overtime. You have exactly 40 hours")
elif hours_worked < 40:
    print("Your gross pay is $", regross_pay, "No overtime. You have under 40 hours")
elif hours_worked > 40:
    print(" Your grosspay is $", otgross_pay, "You have overtime. You have more than 40 hours")
else: 
    print("You did not work this paying period")    








# display the results

