bank_bal = 500
savings_goal = 10000
savings_acct = 2000


#indentation matters each expression and print statement-needs to be align correctly
while bank_bal <= savings_goal:
    bank_bal += savings_acct
    print(f'This week my balance increased to ${bank_bal}')
    if bank_bal == 4500:
        print(f'Almost there! This week my balance is up to ${bank_bal}')
    if bank_bal == 8500:
        bank_bal -= 1000
        print(f'So close! After treating mysel, my balance is up to ${bank_bal}')


print(f'Goal met!My current balance is ${bank_bal}')
  







