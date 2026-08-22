import time


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


# if语句(注意语句顺序，一但先满足条件，后面的语句无效)
has_ticket = True
price = 10.00

if has_ticket:
    print("You may enter, you habe a ticket")
else:
    print("You need to buy a ticket")

if age >= 65:
    print("You are a senior citizen")
    print(f"The tciket price for a senior citizen is ${price * 0.75}")
elif age >= 18:
    print("You are an adult")
    print(f"The tciket price for an audlt is ${price}")
elif age < 0:
    print("You haven't been born yet")
elif age == 0:
    print("You were just born")
else:
    print("You are an child")
    print(f"The tciket price for an child is ${price * 0.5}")


# 逻辑运算符 or and not
temp = 30
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

if temp >= 28 and is_sunny:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif 0 < temp < 28 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")
elif 0 < temp < 28 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")


# while
while name == "":
    name = input("Enter your name: ")
while age < 0:
    age = int(input("Enter your age: "))

print(f"Hello {name}!")
print(f"You are {age} years old!")


# for
name_new = "han jiandong"
for letter in name_new:
    print(letter,end="-")

for i in range(10):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)

for i in range(10, 0, -1):
    print(i)
    #time.sleep(1)
print("HAPPY NEW YEAR!")


# List [] 列表
fruits = ["apple", "orange", "banana", "coconut"]
# fruits[0] = "mango"
# fruits.append("mango")
# fruits.remove("banana")
# fruits.pop(0) #删除索引处的元素
# fruits.clear()

print(fruits)
print(fruits[0])

for fruit in fruits:
    print(fruit, end="")


# Tuple () 元组(元素不可变)
fruits_t = ("apple", "orange", "banana", "coconut")
for fruit in fruits:
    print(fruit, end="")

# Set {} 集合(元素无序不重复，可以添加和删除，但不能重复，也不能通过索引访问)
fruits_s = {"apple", "orange", "banana", "coconut"}
# fruits_s.add("mango")
# fruits_s.remove("apple")

for fruit in fruits:
    print(fruit, end="") # 每次输出顺序不一致

fruit = input("Enter a fruit to saarch for: ")

if fruit in fruits_s:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found")

# function
def happy_birthday(first_name, last_name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old! ")
    return first_name + " " + last_name

names = happy_birthday("han", "jiandong", 24)
print(names)