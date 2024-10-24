# Description:  This script tests various numeric
#               conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
#a2 = int(" 101.1 ") # ValueError: invalid literal for int() with bas 10: ' 101.1 '
a3 = float(a)  
a4 = int(float(a))
a5 = str(a[1:6])
a6 = a.strip()
print(a, type(a))
print(a3, type(a3))
print(a4, type(a4))
print(a5,type(a5))
print(a6, type(a6))

b = '55'
b2 = int('55')
b3 = float('55')
b4 = int(b[:2])
print(b, type(b))
print(b2, type(b2))
print(b3, type(b3))
print(b4, type(b4))

c = "402 Stevens"
#c2 = int("402 Stevens") # ValueError: invalid literal for int() with base 10: '402 stevens'
#c3 = float(c) # ValueError: could not convert string to float: '402 stevens'
c4 = str(c[0:11])
print(c, type(c))
print(c4, type(c4))


d = 'Number 5  '
#d2 = int(d) # ValueError: invalid literal for int() with base 10: 'Number 5  '
#d3 = float(d) # ValueError: could not convert string to float: 'Number 5  '
d4 = str(d[0:8])
d5 = d.strip()
print(d, type(d))
print(d4, type(d4))
print(d5, type(d5))