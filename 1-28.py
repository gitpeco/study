# 循环控制continue中断本次循环和break中断循环

for i in range(1, 19):
    if i == 4:
        continue
    print(i, end=" ")
for j in range(1, 19):
    if j == 4:
        break
    print(j, end='')

# 求水仙花数————每个数位上的数字的3次幂之和等于它本身
# print()
# for a in range(1,10):
#     for b in range(0, 10):
#         for c in range(0, 10):
#             s1 = a*100 + b*10 +c
#             s2 = a**3 + b**3 + c**3
#
#             if s1 == s2:
#                 print(s1, end='  ')

# 使用while
print()
a, b, c = 1, 0, 0
while 1 <= a < 10:
    b=0
    while 0 <= b < 10:
        c=0
        while 0 <= c < 10:

            s1 = a * 100 + b * 10 + c
            s2 = a ** 3 + b ** 3 + c ** 3
            if s1 == s2:
                print(s1, end='  ')
            c = c + 1
        b += 1
    a+=1