dict1 = {
'name': 'Theodore Roosevelt',
'address': '5881 S Parkside Ave',
'city': 'Zion',
'state': 'IL',
'zip': 60688
}

mailing_add = f"""{dict1.get('name')}
{dict1.get('address')}
{dict1.get('city')}, {dict1.get('state')} {dict1.get('zip')}
"""
print(mailing_add)
      
del dict1['name']

full_name = ({'firstname': 'Jon'}), ({'lastname': 'Doe'})
dict1.update({'honorific': 'Mr./Ms./Mx./Dr./Hon.'})

mailing_add2 = f"""{dict1.get('honorific')}
{full_name}
{dict1.get('address')}
{dict1.get('city')}, {dict1.get('state')} {dict1.get('zip')}
"""
print(mailing_add2)
