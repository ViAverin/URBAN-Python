def print_params(a=1, b='str',c=True):
    print(a, b, c)


print_params(b = 25)
print_params(1, 2, 3)

values_list = [1, 'str', (1,2,3)]

values_dict = {"a": 'team', 'b': (1, 8, 3), "c": False}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [True, {1: 'Div'}]
print_params(*values_list_2, 42)