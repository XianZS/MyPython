import array

# array只能存放指定类型的数据
my_array = array.array("i")
my_array.append(1)
my_array.append(2)
print(my_array)
for item in my_array:
    print(item)
