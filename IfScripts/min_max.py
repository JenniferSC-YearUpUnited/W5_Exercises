a = 500
b = 100
c = 1

if a < b and  a < c:
    print(f'{a} is the min') 
if a > b and a > c:
    print(f'{a} is the max')       
if c > a and c > b:
    print(f'{c} is the max')
if b > a and b > c:
    print(f'{b} is the max')
if b < a and b < c:
    print(f'{b} is the min')  
if c < a and c < b:
    print(f'{c} is the min')     
else:
    print("invalid error!")