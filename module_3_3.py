def print_params(a = 13, b = 'string', c = True):
    print(a, b, c)

print('__1__')

print_params()
print_params(b=25)
print_params(c = [1,2,3])

print('__2__')

value_list = [15, 'Verikon', 1.3]
value_dict = {'a': 56, 'b': 'malina', 'c': 1.6}
print_params(*value_list)
print_params(**value_dict)

print('__3__')

values_list_2 = [777, 'СемьСемьСемь']
print_params(*values_list_2, 42)
































