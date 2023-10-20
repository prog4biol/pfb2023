import re

file_h = open('test_file.txt', 'r')
file_o = open('test_file_out.txt', 'w')


my_string = ''


for x in file_h:
    my_string = my_string + x 





my_match = re.finditer(r'[A-Z]IRSTEN', my_string)

for found in my_match:
    file_o.write(f'{found.group(0)}\t')
    file_o.write(f'{found.start()}\t')
    file_o.write(f'{found.end()}\n')




    
## playing with list comprehensions
#my_list = ['1', '2', '3', '4']

#print([type(int(x)) for x in my_list])

