import math
acct= 10000
rule=72
rate=.06
rate2=6
years= rule/rate2
acct_worth=acct*2
print(" At a " + format(rate, ".0%") + " interest rate, your savings account will be worth " + format(acct_worth, ".2f") + " in " + format(years, ".1f") + " years ")