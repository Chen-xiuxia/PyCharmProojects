# 数字字面量
a = 0b1010
b = 100
c = 0o310
d = 0x12c
print(a, b, c, d)
# 浮点字面量
float1=10.5
float2=1.5e2
print(float1, float2)
# 复数字面量
complex1 = 1+3.14j
complex2 = 1+5j
print(complex1,complex1.imag, complex1.real, complex2, complex2.imag, complex2.real)
a = {1,2,2,3,3,3}
print(a)
ac= tuple({1,2,3,4,5})
print(ac)
ab=set(ac)
print(ab)
ad=list(ab)
print(ad)