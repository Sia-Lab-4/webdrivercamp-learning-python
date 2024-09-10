#!/usr/bin/python3
number = 3.141592653589793238
print(f'''
Learning Python is fun"' - {number:.2f} %
''')
print('''
Learning Python is fun"' - {:.2f} %
'''.format(number))
print('''
Learning Python is fun"' - %.2f %%
''' % (number))
