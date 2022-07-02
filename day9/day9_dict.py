programming_dict = {
    'Bug': 'An error that prevents the code from running as expected',
    'Function': 'A piece of code that you can easily call over and over again',
    'Loop': 'The action of doing something over and over again'
}

print(programming_dict)
print(programming_dict.get('Data types'))  # returns none
programming_dict['Data types'] = 'Types such as int, float, bool and others'
print(programming_dict)
print(programming_dict.get('Data types'))

for key in programming_dict:
    print(key)
