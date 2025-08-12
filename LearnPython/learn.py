# 数字字面量
a = 0b1010
b = 100
c = 0o310
d = 0x12c
print(a, b, c, d)
# 浮点字面量
float1 = 10.5
float2 = 1.5e2
print(float1, float2)
# 复数字面量
complex1 = 1 + 3.14j
complex2 = 1 + 5j
print(complex1, complex1.imag, complex1.real, complex2, complex2.imag, complex2.real)
a = {1, 2, 2, 3, 3, 3}
print(a)
ac = tuple({1, 2, 3, 4, 5})
print(ac)
ab = set(ac)
print(ab)
ad = list(ab)
print(ad)
################################################################
num = 3
if num > 0:
    print("正数")
num = -1
if num < 0:
    print("负数")
###################################################################
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0
for i in numbers:
    sum = sum + i
print(sum)

print(range(10))

print(list(range(10)))

print(list(range(2, 8)))

print(list(range(2, 20, 3)))  # 开始，停止，步长 前闭后开区间。前面取的到后面取不到

# 使用索引遍历列表的程序

genre = ['pop', 'rock', 'jazz']

# 使用索引遍历列表
for i in range(len(genre)):
    print("I like", genre[i])

# 显示记录中学生成绩的程序
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('没有找到该名称的条目.')

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%d" % (j, i, i * j), end="\t")
    print()
