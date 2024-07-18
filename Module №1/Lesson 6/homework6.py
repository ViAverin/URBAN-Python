my_dict = {'Victor': 2003, 'Angelina': 2013, 'Daniel': 2006}
print(my_dict)
my_dict['Sasha'] = 2010
print(my_dict.get('Victor'))
print(my_dict.get('Sasha'))
my_dict.update({'Max': 1996,
                'Pavel': 2004})
print(my_dict)
a = my_dict.pop('Angelina')
print(a)
print(my_dict)

my_set = {1, 2, 3, 4, 5, 4, 3, 2, 1, "Hello", True, (1, 2, 3, 4, 5)}
print(my_set)
my_set.add(6)
my_set.add("world")
my_set.discard(5)
print(my_set)