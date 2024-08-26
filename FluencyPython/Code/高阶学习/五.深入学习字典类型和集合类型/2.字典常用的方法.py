"""
    dict()
"""
import copy

print()
student_dict = {
    "jom": {"school": "图灵学院-Python"},
    "kom": {"school": "图灵学院-Rust"}
}

"""
    code(1):浅拷贝
"""
new_dict_1 = student_dict.copy()
new_dict_1["jom"]["school"] = "图灵学院-Go"
print(new_dict_1)
print(student_dict)
print("-" * 50)

"""
    code(2):深拷贝
"""
new_dict_2 = copy.deepcopy(student_dict)
new_dict_2["kom"]["school"] = "图灵学院-C"
print(new_dict_2)
print(student_dict)
print("-" * 50)

"""
    code(3):fromkeys
    fromkeys批量生成字典
"""
student_name = ["jom", "kom"]
new_dict_3 = dict.fromkeys(student_name, {"address": "长沙"})
print(new_dict_3)
print("-" * 50)

"""
    items,输出key和value的数值
"""
for key, value in student_dict.items():
    print(key, value)
print("-" * 50)

"""
    setdefault:
        查询不存在的key，并且设置value
"""
default_value = student_dict.setdefault("lom", {"school": "图灵学院-R"})
print(default_value)
print(student_dict)
print("-" * 50)

"""
    update:当前方法支持接受迭代对象
"""
student_dict.update({"hom": {"school": "图灵学院-matlab"}})
print(student_dict)
student_dict.update(gom={"school": "图灵学院-C++"})
print(student_dict)
# 接受迭代对象
student_dict.update([("fom", {"school": "；图灵学院-C#"}), ("dom", {"school": "图灵学院-Java"})])
print(student_dict)
