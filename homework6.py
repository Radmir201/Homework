# 1
b = [4,5,2,4,3,5,2,1]
print(b)
del b[:4]
del b[1:3]
print(b)

# 2
a=[1,2,3,4,5,6,7,]
n=3
b= [a[i:i + n] for i in range(0, len(a), n)]
print(b)
# 3

a = [1, 2, 3, 4, 5, 6, 7, ]
less_than_5 = []
more_than_5 = []
for num in a:
    if num <= 5:
        less_than_5.append(num)
else:
    more_than_5.append(num)
print("Меньше либо равно пяти:", less_than_5)
print("Больше пяти:", more_than_5)

# 4
name = input("Введите имя: ")
surname = input("Введите фамилию: ")
age = input("Введите возраст: ")
user_info = [name, surname, age]
print(user_info)

# 5

problem = input("Введите пример со сложением: ")
result = eval(problem)
print(result)

# 6
