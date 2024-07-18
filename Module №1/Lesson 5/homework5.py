immutable_var = 1, 2, 3, 4, True, "Hello world"
print(immutable_var)
print(type(immutable_var))
# Кортеж неизменяем. К неизменяемым объектам относятся числа и строки.
# immutable_var[0] = 200
# print(immutable_var[0])

mutable_list = [1, 2, 3, 4, True, "Hello world"]
print(mutable_list)
print(type(mutable_list))
mutable_list[0] = 4
mutable_list[1] = 3
mutable_list[2] = 2
mutable_list[3] = 1
print(mutable_list)
