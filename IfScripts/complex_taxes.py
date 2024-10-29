pay_rate=22.25
hours_worked=40
#othours = 0
regross_pay= pay_rate * hours_worked
#otgross_rate = (1.5 *pay_rate)* othours
#otgross_pay = otgross_rate + regross_pay 
#if hours_worked == 40:
   # print("Your gross pay is $", regross_pay, "No overtime. You have exactly 40 hours")
#elif hours_worked < 40:
 #   print("Your gross pay is $", regross_pay, "No overtime. You have under 40 hours")
#elif hours_worked > 40:
 #   print(" Your grosspay is $", otgross_pay, "You have overtime. You have more than 40 hours")
#else: 
 #   print("You did not work this paying period")    

# weeks in a year by weekly grosspay for annual gross pay
ann_regross_pay = regross_pay * 52
print(f'''Your annual regular gross income is:
      ${format(ann_regross_pay, ".2f")}''')


# single filers
if ann_regross_pay < 12000.0 : 
     print("Your single filers tax rate is: " + format(.05, ".0%"))
elif ann_regross_pay >= 12000.0 and ann_regross_pay <= 24999.99:
    print("Your single filers tax rate is: " + format(.10, ".0%"))
elif ann_regross_pay >= 25000.0 and ann_regross_pay <= 74999.99:  
    print(" Your single filers tax rate is: " + format(.15, ".0%"))
elif ann_regross_pay >= 75000.0:
    print("Your single filers tax rate is : " + format(.2, ".0%"))
else:
     print("Annual income range for single filers is invalid")


# joint filers
if ann_regross_pay < 12000.0:
     print("Your joint filers tax rate is: " + format(.0, ".0%"))
elif ann_regross_pay >= 12000.0 and ann_regross_pay <= 24999.99:
     print("Your joint filers tax rate is: " + format(.06, ".0%"))   
elif ann_regross_pay >= 25000.0 and ann_regross_pay <= 74999.99:
     print("Your joint filers tax rate is: " + format(.11, ".0%"))
elif ann_regross_pay >= 75000.0:
    print("Your joint filers tax rate is: " + format(.2, ".0%"))
else:
    print("Annual income range for joint filers is invalid")    
                          


#weekly gross pay single filers
tax_amount1 = regross_pay * .05
tax_withheld1 = regross_pay - tax_amount1

tax_amount2 = regross_pay *.10
tax_withheld2 = regross_pay - tax_amount2

tax_amount3 = regross_pay *.15
tax_withheld3 = regross_pay - tax_amount3

tax_amount3 = regross_pay * .2 
tax_withheld4 = regross_pay - tax_amount3 




print(f'''You worked {hours_worked} hours this period. Because you earn ${format(pay_rate, ".2f")},
your gross weekly pay is ${format(regross_pay, ".2f")}. Your filing status is single. Your tax witholding for the week is ${format(tax_amount1, ".2f")}. Your net pay is ${format(tax_withheld1, ".2f")}.''')
