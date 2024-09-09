"""
    列表推导式
"""
int_list_1 = [i for i in range(1, 21) if i & 1]
print(int_list_1)


def handle_item(item):
    return item * item


int_list_2 = [handle_item(i) for i in range(1, 21) if i & 1]
print(int_list_2)

"""
    生成器推导式
"""
int_gen = (i for i in range(1, 21) if i & 1)
print(int_gen)
print(next(int_gen))
# 1
print(next(int_gen))
# 3
print(next(int_gen))
# 5
print(list(int_gen))
# [7, 9, 11, 13, 15, 17, 19]

"""
    字典推导式
"""
my_dict = {"name": "jom", "age": 21, "address": "上海"}
reversed_my_dict = {value: key for key, value in my_dict.items()}
print(reversed_my_dict)

"""
    集合推导式
"""
int_set = {i for i in range(1, 21) if i & 1}
print(int_set)
