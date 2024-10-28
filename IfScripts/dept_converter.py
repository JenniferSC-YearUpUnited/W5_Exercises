# Looksups = dictionary
# define known values
depart_names = {1: 'Marketing',
                5: 'Human Resources',
                10: 'Accounting',
                12: 'Legal',
                18: 'IT',
                20: 'Customer Relations'
                }


departcode = int(input('Please enter one dept code from the list for dept name: 1, 5 , 10, 12, 18, 20 '))
# calculate unknown values
# display results
if departcode == 1:
    print(depart_names.get(1))
elif departcode == 5:
    print(depart_names.get(5))
elif departcode == 10:
    print(depart_names.get(10))
elif departcode == 12:
    print(depart_names.get(12))
elif departcode == 18:
    print(depart_names.get(18))
elif departcode == 20:
    print(depart_names.get(20))
else:
    print('Invalid Department Code!')                    

    
    

