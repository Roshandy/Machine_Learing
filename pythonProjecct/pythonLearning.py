full_name = "Bro Code"
age = 25
gpa = 3.8
is_student = True

print (f"Hello {full_name}")
print(f"You are {age} years old")
print(f"Your gpa is {gpa}")
print(f"Are you a student?: {is_student}")

if is_student:
    print("you are a steudent")
else:
    print ("you are NOT a student")

# arithmetic(+ - * / // %) 算术运算
friends = 5
# friends = friends + 2
friends += 2
# // 除法（向下取整）
# % 取模

print(friends)

# Typecasting 类型转换 str() int() float() bool()
age = float(age)
print(age)
print(type(age))

age = str(age)
age += "1"
print(age)

# 字符串为空时，才会输出false
full_name = bool(full_name)
print(full_name)

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
age += 1
print(type(name))
print(type(age))
print(f"Hello {name}")
print(f"you are {age} years old")

