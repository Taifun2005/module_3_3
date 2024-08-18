def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(a ='test', b = 'первая', c ='строчка')
print_params(a ='строчка', b = 'вторая')
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = ('Тест', True, 87)
values_dict ={"a":'test', "b":True, "c":78}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ('Тест', 100)
print_params(*values_list_2, 42)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)